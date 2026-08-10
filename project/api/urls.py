from django.urls import path
from . import views

urlpatterns = [
	path('mopcat/', views.APIProjMopCat.as_view()),
	path('cat/', views.APIProjCat.as_view()),
	path('cap/', views.APIProjCap.as_view()),
	path('sec/', views.APIProjSec.as_view()),
]