from django.urls import path
from . import views

urlpatterns = [
	path('', views.NewsList, name='admin-news-list'),
    path('add/', views.NewsAdd, name='admin-news-add'),
    path('edit/<str:hashid>/', views.NewsEdit, name='admin-news-edit'),
    path('detail/<str:hashid>/', views.NewsDetail, name='admin-news-det'),
    path('rem/<str:pk>/', views.NewsRem, name='admin-news-rem'),
    path('ena/<str:hashid>/', views.NewsEnable, name='admin-news-ena'),
    path('dis/<str:hashid>/', views.NewsDisable, name='admin-news-dis'),
    path('mainyes/<str:pk>/', views.NewsMainYes, name='admin-news-mainyes'),
    path('mainno/<str:pk>/', views.NewsMainNo, name='admin-news-mainno'),
    path('headline/<str:pk>/', views.NewsHeadline, name='admin-news-headline'),
    path('image/add/<str:hashid>/', views.NewsImageAdd, name='admin-newsimg-add'),
    path('image/edit/<str:hashid>/<str:pk>/', views.NewsImageEdit, name='admin-newsimg-edit'),
]