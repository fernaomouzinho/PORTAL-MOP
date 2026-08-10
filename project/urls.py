from django.urls import path
from . import views

urlpatterns = [
	path('dash/', views.ProjDash, name="admin-proj-dash"),
	path('portal/home/', views.PortalHomeList, name="admin-portal-home"),
	path('portal/home/sync/', views.PortalHomeSync, name="admin-portal-home-sync"),
	path('portal/home/ena/', views.PortalHomeEna, name="admin-portal-home-ena"),
	path('portal/home/dis/', views.PortalHomeDis, name="admin-portal-home-dis"),
    #
	path('mopcat/', views.ProjMopCatList, name="admin-proj-mopcat"),
	path('mopcat/sync/', views.ProjMopCatSync, name="admin-proj-mopcat-sync"),
	path('mopcat/ena/', views.ProjMopCatEna, name="admin-proj-mopcat-ena"),
	path('mopcat/dis/', views.ProjMopCatDis, name="admin-proj-mopcat-dis"),
    #
	path('cat/', views.ProjCatList, name="admin-proj-cat"),
	path('cat/sync/', views.ProjCatSync, name="admin-proj-cat-sync"),
	path('cat/ena/', views.ProjCatEna, name="admin-proj-cat-ena"),
	path('cat/dis/', views.ProjCatDis, name="admin-proj-cat-dis"),
    #
	path('cap/', views.ProjCapList, name="admin-proj-cap"),
	path('cap/sync/', views.ProjCapSync, name="admin-proj-cap-sync"),
	path('cap/ena/', views.ProjCapEna, name="admin-proj-cap-ena"),
	path('cap/dis/', views.ProjCapDis, name="admin-proj-cap-dis"),
    #
	path('sec/', views.ProjSecList, name="admin-proj-sec"),
	path('sec/sync/', views.ProjSecSync, name="admin-proj-sec-sync"),
	path('sec/ena/', views.ProjSecEna, name="admin-proj-sec-ena"),
	path('sec/dis/', views.ProjSecDis, name="admin-proj-sec-dis"),
    #
	path('cont/list/', views.ContList, name="admin-proj-cont-list"),
	path('cont/hist/', views.ContHist, name="admin-proj-cont-hist"),
    #
	path('map/g/list/', views.ProjMapGList, name="admin-map-g-list"),
	path('map/g/view/<str:pk>/', views.ProjMapGView, name="admin-map-g-view"),
	path('map/g/add/', views.ProjMapGAdd, name="admin-map-g-add"),
	path('map/g/edit/<str:pk>/', views.ProjMapGEdit, name="admin-map-g-edit"),
	path('map/g/rem/<str:pk>/', views.ProjMapGRem, name="admin-map-g-rem"),
	path('map/g/ena/<str:pk>/', views.ProjMapGEna, name="admin-map-g-ena"),
    #
	path('map/s/list/', views.ProjMapSList, name="admin-map-s-list"),
	path('map/s/view/<str:pk>/', views.ProjMapSView, name="admin-map-s-view"),
	path('map/s/add/', views.ProjMapSAdd, name="admin-map-s-add"),
	path('map/s/edit/<str:pk>/', views.ProjMapSEdit, name="admin-map-s-edit"),
	path('map/s/rem/<str:pk>/', views.ProjMapSRem, name="admin-map-s-rem"),
	path('map/s/ena/<str:pk>/', views.ProjMapSEna, name="admin-map-s-ena"),
    #
	path('map/p/list/', views.ProjMapPList, name="admin-map-p-list"),
	path('map/p/view/<str:pk>/', views.ProjMapPView, name="admin-map-p-view"),
	path('map/p/add/', views.ProjMapPAdd, name="admin-map-p-add"),
	path('map/p/edit/<str:pk>/', views.ProjMapPEdit, name="admin-map-p-edit"),
	path('map/p/rem/<str:pk>/', views.ProjMapPRem, name="admin-map-p-rem"),
	path('map/p/ena/<str:pk>/', views.ProjMapPEna, name="admin-map-p-ena"),
]