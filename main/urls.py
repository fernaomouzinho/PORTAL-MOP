from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.inisiu, name='inisiu'),
    path('<str:lang>/home/', views.home, name='home'),
    path('<str:lang>/about/', views.AboutView, name='about'),
    path('<str:lang>/orgchart/', views.OrgView, name='orgchart'),
    path('<str:lang>/dgs/', views.DGList, name='dg-list'),
    path('<str:lang>/dgs/<str:pk>/', views.DGDet, name='dg-det'),
    path('<str:lang>/divs/', views.DivList, name='div-list'),
    path('<str:lang>/divs/<str:pk>/', views.DivDet, name='div-det'),
    path('<str:lang>/otdivs/', views.OtDivList, name='otdiv-list'),
    path('<str:lang>/otdiv/<str:pk>/', views.OtDivDet, name='otdiv-det'),
    path('<str:lang>/doc/', views.DocList, name='doc-list'),
    path('<str:lang>/doc/<str:hashid>/', views.DocDetail, name='doc-det'),
    # path('doc/list/<str:lang>/', views.DocList, name='doc-list'),
    # path('doc/det/<str:lang>/<str:hashid>/', views.DocDetail, name='doc-det'),
    path('<str:lang>/reports/', views.ReportList, name='report-list'),
    path('<str:lang>/reports/<str:hashid>/', views.ReportDetail, name='report-det'),
    path('<str:lang>/reports/<str:dg>/list/', views.ReportListDg, name='report-dg-list'),
    path('<str:lang>/reports/year/<str:yr>/', views.ReportYearList, name='report-year-list'),
    path('<str:lang>/reports/year/<str:yr>/<str:dg>/', views.ReportYearListDg, name='report-year-dg-list'),
    #
    path('<str:lang>/news/', views.listNews, name='news-list'),
    path('<str:lang>/news/<slug:cat>/', views.listCatNews, name='news-cat-list'),
    path('<str:lang>/news/<slug:cat>/year/<str:year>/', views.listCatNewsYear, name='news-cat-year-list'),
    path('<str:lang>/news/<slug:cat>/year/<str:year>/<str:month>/', views.listCatNewsYearMonth, name='news-cat-year-month-list'),
    path('<str:lang>/news/<str:year>/<str:month>/<str:hashid>/<slug:titleseo>/', views.detailNews, name='news-detail'),
    path('<str:lang>/news/year/<str:year>/', views.listNewsYear, name='news-year'),
    path('<str:lang>/news/year/<str:year>/<str:month>/', views.listNewsMonth, name='news-month'),
    #
    path('<str:lang>/team/detail/<str:pk>/', views.TeamDetail, name='team-det'),
    #
    path('<str:lang>/proj/sum/', views.ProjSum, name='proj-sum'),
    
    path('<str:lang>/proj/list/', views.ProjList, name='proj-list'),
    path('<str:lang>/proj/hist/', views.ProjHist, name='proj-hist'),
    path('<str:lang>/proj/map/g/view/', views.ProjMapGView, name='proj-map-g-view'),
    path('<str:lang>/proj/map/s/view/', views.ProjMapSView, name='proj-map-s-view'),
    path('<str:lang>/proj/map/p/view/', views.ProjMapPView, name='proj-map-p-view'),
    
    #
    path('<str:lang>/vaga/list/', views.VagaList, name='vaga-list'),
    path('<str:lang>/vaga/detail/<str:hashid>/', views.VagaDetail, name='vaga-det'), 
    path('<str:lang>/tender/list/', views.TenderList, name='tender-list'),
    path('<str:lang>/tender/detail/<str:hashid>/', views.TenderDetail, name='tender-det'), 
    path('<str:lang>/ann/list/', views.AnnList, name='ann-list'),
    path('<str:lang>/ann/detail/<str:hashid>/', views.AnnDetail, name='ann-det'), 
    #
    path('<str:lang>/images/', views.AlbumList, name='album'),
    path('<str:lang>/images/<str:hashid>/', views.GalleryList, name='gallery'), 
    path('<str:lang>/images/det/<str:hashid>/', views.GalleryDet, name='gallery-det'), 
    path('<str:lang>/video/', views.VideoList, name='video'),
    path('<str:lang>/contact/', views.ContactView, name='contact'),
    
    ]