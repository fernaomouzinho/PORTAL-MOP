
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from main import views as main_views
from web_admin.views import admin_home
from django.conf.urls import handler404, handler500
from django.views.static import serve

admin.site.site_header = 'MOP-PORTAL SUPER USER'

urlpatterns = [
    path('mopportaladmin23/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='web_admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='web_admin/logout.html'), name='logout'),
    path('summernote/', include('django_summernote.urls')),
    
    path('portaladmin/', admin_home, name='admin_home'),
    path('portaladmin/about/', include('about.urls')),
    path('portaladmin/custom/', include('custom.urls')),
    path('portaladmin/news/', include('news.urls')),
    path('portaladmin/doc/', include('doc.urls')),
    path('portaladmin/ann/', include('announce.urls')),
    path('portaladmin/mul/', include('multimedia.urls')),
    path('portaladmin/pub/', include('pub.urls')),
    path('portaladmin/proj/', include('project.urls')),
    path('api/proj/', include('project.api.urls')),
    path('portaladmin/users/', include('users.urls')),
    path('api/', include('web_admin.api.urls')),
    path('', include('main.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]  

handler404 = 'errors.views.error_404'
handler500 = 'errors.views.error_500'

# if settings.DEBUG:
	# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)