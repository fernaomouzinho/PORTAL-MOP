import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from project.models import ProjMapG, ProjMapS, ProjMapP
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMapGList(request):
	roles = get_roles(request)
	objects = ProjMapG.objects.filter().all()
	context = {
		'group': roles, 'objects': objects,
		'title': 'Mapa Projetu', 'legend': 'Mapa Projetu'
	}
	return render(request, 'project_map/map_g_list.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMapGView(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(ProjMapG, pk=pk)
	context = {
		'group': roles, 'objects': objects, 'page': 'mapg',
		'title': 'Mapa Projetu', 'legend': 'Mapa Projetu'
	}
	return render(request, 'project_map/map_g_view.html', context)
#
@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMapSList(request):
	roles = get_roles(request)
	objects = ProjMapS.objects.filter().all()
	context = {
		'group': roles, 'objects': objects,
		'title': 'Mapa Status Projetu', 'legend': 'Mapa Status Projetu'
	}
	return render(request, 'project_map/map_s_list.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMapSView(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(ProjMapS, pk=pk)
	context = {
		'group': roles, 'objects': objects, 'page': 'maps',
		'title': 'Mapa Status rojetu', 'legend': 'Mapa Status Projetu'
	}
	return render(request, 'project_map/map_s_view.html', context)
#
@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMapPList(request):
	roles = get_roles(request)
	objects = ProjMapP.objects.filter().all()
	context = {
		'group': roles, 'objects': objects,
		'title': 'Mapa Progresu Projetu', 'legend': 'Mapa Progresu Projetu'
	}
	return render(request, 'project_map/map_p_list.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMapPView(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(ProjMapP, pk=pk)
	context = {
		'group': roles, 'objects': objects, 'page': 'maps',
		'title': 'Mapa Progresu rojetu', 'legend': 'Mapa Progresu Projetu'
	}
	return render(request, 'project_map/map_p_view.html', context)
