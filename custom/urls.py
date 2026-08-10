from django.urls import path
from . import views

urlpatterns = [
	path('dg/list/', views.DGList, name="admin-dg-list"),
	path('dg/det/<str:pk>/', views.DGDet, name="admin-dg-det"),
	path('dg/add/', views.DGAdd, name="admin-dg-add"),
	path('dg/edit/<str:pk>/', views.DGEdit, name="admin-dg-edit"),
    #
	path('div/list/', views.DivList, name="admin-div-list"),
	path('div/det/<str:pk>/', views.DivDet, name="admin-div-det"),
	path('div/add/', views.DivAdd, name="admin-div-add"),
	path('div/edit/<str:pk>/', views.DivEdit, name="admin-div-edit"),
    #
	path('otdiv/list/', views.OtDivList, name="admin-otdiv-list"),
	path('otdiv/det/<str:pk>/', views.OtDivDet, name="admin-otdiv-det"),
	path('otdiv/add/', views.OtDivAdd, name="admin-otdiv-add"),
	path('otdiv/edit/<str:pk>/', views.OtDivEdit, name="admin-otdiv-edit"),
]