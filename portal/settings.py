from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8gx4w-05+l_8=!vfsrl&a=z(#rhw_^4b8z^cf_^&w3c7jo^(^p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'crispy_forms',
    'django_cleanup',
    'rest_framework',
    'django_summernote',
    'imagekit',
    'mathfilters',
    'django_social_share',
    'main.apps.MainConfig',
	'web_admin.apps.WebAdminConfig',
    'custom.apps.CustomConfig',
    'about.apps.AboutConfig',
    'news.apps.NewsConfig',
    'multimedia.apps.MultimediaConfig',
    'doc.apps.DocConfig',
    'announce.apps.AnnounceConfig',
    'pub.apps.PubConfig',
    'project.apps.ProjectConfig',
    'users.apps.UsersConfig',
    'errors.apps.ErrorsConfig',
    'crispy_bootstrap4',
    'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'portal.middleware.PortalSSOMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portal.views.front_end',
            ],
        },
    },
]

WSGI_APPLICATION = 'portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'smartvps04_portal',
        'USER': 'root',
        'PASSWORD': 'atauro2630',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET NAMES 'utf8mb4' COLLATE 'utf8mb4_general_ci'; SET foreign_key_checks = 0;",
        },
    }
    
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'smartvps04_portal',
    #     'USER': 'mopdbuser',
    #     'PASSWORD': '23#MOP_sigp@',
    #     'HOST': 'mysql.s1635.sureserver.com',
    #     'PORT': '3308',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #     },
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# LOGIN_REDIRECT_URL = 'admin_home'

# LOGIN_URL = 'login'

# ABSOLUTE_URL_OVERRIDES = {
# 	'auth.user': lambda u: "/users/users/",
# }

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
		message_constants.INFO: 'info',
		message_constants.SUCCESS: 'success',
		message_constants.WARNING: 'warning',
		message_constants.ERROR: 'danger',}

X_FRAME_OPTIONS = 'SAMEORIGIN'

SESSION_COOKIE_NAME = "portal_sessionid"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
BASE_DIRs = Path(__file__).resolve().parent

# Load PUBLIC key
with open(BASE_DIRs / "key" / "public.pem", "r") as f:
    PUBLIC_KEY = f.read()

SIMPLE_JWT = {
    "ALGORITHM": "RS256",
    "VERIFYING_KEY": PUBLIC_KEY,
    "SIGNING_KEY": None,
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

SSO_CHECK_INTERVAL = 5
