from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.AnnounceList, name='admin-ann-list'),
	path('add/', views.AnnounceAdd, name='admin-ann-add'),
	path('edit/<str:hashid>/', views.AnnounceEdit, name='admin-ann-edit'),
	path('detail/<str:hashid>/', views.AnnounceDetail, name='admin-ann-det'),
	path('ena/<str:pk>/', views.AnnounceEnable, name='admin-ann-ena'),
	path('dis/<str:pk>/', views.AnnounceDisable, name='admin-ann-dis'),
	path('rem/<str:pk>/', views.AnnounceRem, name='admin-ann-rem'),
	path('pdf/<str:hashid>/', views.AnnouncePDF, name='admin-ann-pdf'),
]