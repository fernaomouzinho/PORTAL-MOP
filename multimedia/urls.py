from django.urls import path
from . import views

urlpatterns = [
	path('banner/list/', views.BannerList, name='admin-banner-list'),
	path('banner/add/', views.BannerAdd, name='admin-banner-add'),
	path('banner/edit/<str:pk>/', views.BannerEdit, name='admin-banner-edit'),
	path('banner/rem/<str:pk>/', views.BannerRem, name='admin-banner-rem'),
	path('banner/ena/<str:pk>/', views.BannerEnable, name='admin-banner-ena'),
	path('banner/dis/<str:pk>/', views.BannerDisable, name='admin-banner-dis'),
	#
	path('album/list/', views.AlbumList, name='admin-album-list'),
	path('album/add/', views.AlbumAdd, name='admin-album-add'),
	path('album/edit/<str:hashid>/', views.AlbumUpdate, name='admin-album-edit'),
	path('album/remove/<str:pk>/',views.AlbumRemove, name='admin-album-rem'),
	path('album/dis/<str:pk>/',views.AlbumDisable, name='admin-album-dis'),
	path('album/ena/<str:pk>/',views.AlbumEnable, name='admin-album-ena'),
	path('album/<str:hashid>/', views.GalleryList, name='admin-gallery-list'),
	path('add/<str:hashid>/', views.GalleryAdd, name='admin-gallery-add'),
	path('edit/<str:hashid>/<str:hashid2>/', views.GalleryEdit, name='admin-gallery-edit'),
	path('remove/<str:hashid>/<str:pk>/', views.GalleryRemove, name='admin-gallery-rem'),
	path('ena/<str:hashid>/<str:pk>/', views.GalleryEnable, name='admin-gallery-ena'),
	path('dis/<str:hashid>/<str:pk>/', views.GalleryDisable, name='admin-gallery-dis'),
    #
	path('video/list/', views.VideoList, name='admin-video-list'),
	path('video/add/', views.VideoAdd, name='admin-video-add'),
	path('video/edit/<str:pk>/', views.VideoEdit, name='admin-video-edit'),
	path('video/rem/<str:pk>/', views.VideoRemove, name='admin-video-rem'),
	path('video/ena/<str:pk>/', views.VideoEnable, name='admin-video-ena'),
	path('video/dis/<str:pk>/', views.VideoDisable, name='admin-video-dis'),
	path('video/main/<str:pk>/', views.VideoMain, name='admin-video-main'),
	path('video/play/<str:pk>/', views.VideoPlay, name='admin-video-play'),
]