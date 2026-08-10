from django.urls import path
from . import views

urlpatterns = [
    #
    path('vaga/list/', views.VagaList, name='admin-vaga-list'),
    path('vaga/add/', views.VagaAdd, name='admin-vaga-add'),
    path('vaga/edit/<str:hashid>/', views.VagaEdit, name='admin-vaga-edit'),
    path('vaga/detail/<str:hashid>/', views.VagaDetail, name='admin-vaga-det'),
    path('vaga/rem/<str:pk>/', views.VagaRem, name='admin-vaga-rem'),
    path('vaga/ena/<str:pk>/', views.VagaEnable, name='admin-vaga-ena'),
    path('vaga/dis/<str:pk>/', views.VagaDisable, name='admin-vaga-dis'),
    path('vaga/pdf/<str:hashid>/', views.VagaPDF, name='admin-vaga-pdf'),
    path('vaga/download/<str:hashid>/', views.VagaDownload, name='admin-vaga-down'),
    #
    path('tender/list/', views.TenderList, name='admin-tender-list'),
    path('tender/add/', views.TenderAdd, name='admin-tender-add'),
    path('tender/edit/<str:hashid>/', views.TenderEdit, name='admin-tender-edit'),
    path('tender/detail/<str:hashid>/', views.TenderDetail, name='admin-tender-det'),
    path('tender/rem/<str:pk>/', views.TenderRem, name='admin-tender-rem'),
    path('tender/ena/<str:pk>/', views.TenderEnable, name='admin-tender-ena'),
    path('tender/dis/<str:pk>/', views.TenderDisable, name='admin-tender-dis'),
    path('tender/pdf/<str:hashid>/', views.TenderPDF, name='admin-tender-pdf'),
    path('tender/download/<str:hashid>/', views.TenderDownload, name='admin-tender-down'),
    #
    path('pub/list/', views.PubList, name='admin-pub-list'),
    path('pub/add/', views.PubAdd, name='admin-pub-add'),
    path('pub/edit/<str:hashid>/', views.PubEdit, name='admin-pub-edit'),
    path('pub/detail/<str:hashid>/', views.PubDetail, name='admin-pub-det'),
    path('pub/rem/<str:pk>/', views.PubRem, name='admin-pub-rem'),
    path('pub/ena/<str:pk>/', views.PubEnable, name='admin-pub-ena'),
    path('pub/dis/<str:pk>/', views.PubDisable, name='admin-pub-dis'),
    path('pub/pdf/<str:hashid>/', views.PubPDF, name='admin-pub-pdf'),
    path('pub/download/<str:hashid>/', views.PubDownload, name='admin-pub-down'),
]