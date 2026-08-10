from django.urls import path
from . import views

urlpatterns = [
	path('about/', views.AboutView, name="admin-about"),
	path('about/edit/', views.AboutEdit, name="admin-about-edit"),
	path('orgchart/edit/', views.OrgChartEdit, name="admin-orgchart-edit"),
	path('orgchart/pdf/', views.OrgChartPDF, name="admin-orgchart-pdf"),
	path('struc/', views.StrucList, name="admin-struc-list"),
	path('struc/add/', views.StrucAdd, name="admin-struc-add"),
	path('struc/edit/<str:pk>/', views.StrucEdit, name="admin-struc-edit"),
	path('struc/det/<str:pk>/', views.StrucDetail, name="admin-struc-det"),
	path('struc/ena/<str:pk>/', views.StrucEna, name="admin-struc-ena"),
	path('struc/dis/<str:pk>/', views.StrucDis, name="admin-struc-dis"),
	path('struc/img/', views.StrucImg, name="admin-struc-img"),
	path('cont/', views.ContView, name="admin-cont-view"),
	path('cont/mun/list/', views.ContMunList, name="admin-cont-mun-list"),
	path('cont/mun/add/', views.ContMunAdd, name="admin-cont-mun-add"),
	path('cont/mun/edit/<str:pk>/', views.ContMunEdit, name="admin-cont-mun-edit"),
    #
	path('partner/list/', views.PartnerList, name="admin-partner-list"),
	path('partner/add/', views.PartnerAdd, name="admin-partner-add"),
	path('partner/edit/<str:pk>/', views.PartnerEdit, name="admin-partner-edit"),
	path('partner/rem/<str:pk>/', views.PartnerRemove, name="admin-partner-rem"),
	path('partner/ena/<str:pk>/', views.PartnerEnable, name="admin-partner-ena"),
	path('partner/dis/<str:pk>/', views.PartnerDisable, name="admin-partner-dis"),
]