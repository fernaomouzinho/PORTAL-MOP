# portal/middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from types import SimpleNamespace
import requests
import logging

logger = logging.getLogger(__name__)


class PortalSSOMiddleware(MiddlewareMixin):

    EXCLUDED_PREFIXES = (
        "/static/",
        "/media/",
        "/favicon.ico",
        "/mopportaladmin23/login/",
    )

    def process_request(self, request):

        path = request.path

        if path.startswith(self.EXCLUDED_PREFIXES):
            return

        # =====================================
        # SESSION MODE
        # =====================================
        if request.session.get("sso_authenticated"):

            self.validate_central_session(request)

            user_id = request.session.get("portal_user_id")
            username = request.session.get("portal_user")
            roles = request.session.get("portal_roles", [])

            # IMPORTANT FIX
            request.user = SimpleNamespace(
                is_authenticated=True,
                id=user_id,
                username=username,
                is_staff=True,
                is_superuser=False,
            )

            request.auth_user = {
                "id": user_id,
                "username": username,
                "roles": roles,
            }

            request.portal_user = username
            request.portal_roles = roles
            return

        # =====================================
        # TOKEN LOGIN MODE
        # =====================================
        token = request.GET.get("token") or request.META.get("HTTP_AUTHORIZATION")

        if not token:
            request.user = AnonymousUser()
            return

        try:
            if token.startswith("Bearer "):
                token = token.split(" ")[1]

            payload = JWTAuthentication().get_validated_token(token).payload

            if payload.get("iss") != "main-system":
                request.user = AnonymousUser()
                return

            username = payload.get("username")
            user_id = payload.get("user_id")
            roles = payload.get("roles", [])

            request.session["sso_authenticated"] = True
            request.session["portal_user_id"] = user_id
            request.session["portal_user"] = username
            request.session["portal_roles"] = roles
            request.session["jwt_jti"] = payload.get("jti")
            request.session["jwt_session_version"] = payload.get("session_version")
            request.session["last_sso_check"] = 0

            request.session.set_expiry(
                getattr(settings, "PORTAL_SESSION_AGE", 28800)
            )

            # IMPORTANT FIX
            request.user = SimpleNamespace(
                is_authenticated=True,
                id=user_id,
                username=username,
                is_staff=True,
                is_superuser=False,
            )

            request.auth_user = {
                "id": user_id,
                "username": username,
                "roles": roles,
            }

            request.portal_user = username
            request.portal_roles = roles

        except Exception as e:
            logger.warning("JWT ERROR: %s", str(e))
            request.user = AnonymousUser()

    def validate_central_session(self, request):

        import time

        now = int(time.time())
        interval = getattr(settings, "SSO_CHECK_INTERVAL", 120)

        last = request.session.get("last_sso_check", 0)

        if now - last < interval:
            return

        request.session["last_sso_check"] = now

        try:
            res = requests.get(
                "http://127.0.0.1:8000/check-session/",
                params={
                    "jti": request.session.get("jwt_jti"),
                    "user_id": request.session.get("portal_user_id"),
                    "session_version": request.session.get("jwt_session_version"),
                },
                timeout=2
            )

            if res.status_code == 200:
                if not res.json().get("active"):
                    request.session.flush()

        except Exception:
            pass