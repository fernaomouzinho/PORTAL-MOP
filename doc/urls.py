from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.DocList, name='admin-doc-list'),
	path('add/', views.DocAdd, name='admin-doc-add'),
	path('edit/<str:hashid>/', views.DocEdit, name='admin-doc-edit'),
	path('detail/<str:hashid>/', views.DocDetail, name='admin-doc-det'),
	path('ena/<str:pk>/', views.DocEnable, name='admin-doc-ena'),
	path('dis/<str:pk>/', views.DocDisable, name='admin-doc-dis'),
	path('rem/<str:pk>/', views.DocRem, name='admin-doc-rem'),
	path('pdf/<str:hashid>/', views.DocPDF, name='admin-doc-pdf'),
    #
    path('report/list/', views.ReportList, name='admin-report-list'),
    path('report/add/', views.ReportAdd, name='admin-report-add'),
    path('report/edit/<str:hashid>/', views.ReportEdit, name='admin-report-edit'),
    path('report/detail/<str:hashid>/', views.ReportDetail, name='admin-report-det'),
    path('report/rem/<str:pk>/', views.ReportRem, name='admin-report-rem'),
    path('report/ena/<str:pk>/', views.ReportEnable, name='admin-report-ena'),
    path('report/dis/<str:pk>/', views.ReportDisable, name='admin-report-dis'),
    path('report/pdf/<str:hashid>/', views.ReportPDF, name='admin-report-pdf'),
    path('report/download/<str:hashid>/', views.ReportDownload, name='admin-report-down'),
]