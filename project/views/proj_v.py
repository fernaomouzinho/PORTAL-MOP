from django.shortcuts import render
from project.models import PortalHome, ProjCat, ProjCap, ProjMopCat, ProjSec
from users.decorators import allowed_users
from project.read_api import read_portal_home, read_proj_cat, read_proj_cap, read_proj_mopcat, read_proj_sec,\
	read_cont_list, read_cont_hist
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjDash(request):
	roles = get_roles(request)
	context = {
		'group': roles,'title': 'Painel Projetu', 'legend': 'Painel Projetu'
	}
	return render(request, 'project/dash.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def PortalHomeList(request):
	roles = get_roles(request)
	read = read_portal_home()
	obj = PortalHome.objects.first()
	context = {
		'group': roles, 'read': read, 'obj': obj,
		'title': 'Portal Home', 'legend': 'Portal Home'
	}
	return render(request, 'project/portal_home.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMopCatList(request):
	roles = get_roles(request)
	read = read_proj_mopcat()
	obj = ProjMopCat.objects.first()
	context = {
		'group': roles, 'read': read, 'obj': obj,
		'title': 'Kategoria Projetu - MOP', 'legend': 'Kategoria Projetu - MOP'
	}
	return render(request, 'project/proj_mopcat.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjCatList(request):
	roles = get_roles(request)
	read = read_proj_cat()
	obj = ProjCat.objects.first()
	context = {
		'group': roles, 'read': read, 'obj': obj,
		'title': 'Kategoria Projetu', 'legend': 'Kategoria Projetu'
	}
	return render(request, 'project/proj_cat.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjCapList(request):
	roles = get_roles(request)
	read = read_proj_cap()
	obj = ProjCap.objects.first()
	context = {
		'group': roles, 'read': read, 'obj': obj,
		'title': 'Capital Orsamentu', 'legend': 'Capital Orsamentu'
	}
	return render(request, 'project/proj_cap.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjSecList(request):
	roles = get_roles(request)
	read = read_proj_sec()
	obj = ProjSec.objects.first()
	context = {
		'group': roles, 'read': read, 'obj': obj,
		'title': 'Setor Projetu', 'legend': 'Setor Projetu'
	}
	return render(request, 'project/proj_sec.html', context)
# cont
@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ContList(request):
	roles = get_roles(request)
	read = read_cont_list()
	objects = []
	for i in read['objects']:
		objects.append(i)
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Projetu nebe Lao Hela (Ongoing)', 'legend': 'Lista Projetu nebe Lao Hela (Ongoing)'
	}
	return render(request, 'project/cont_list.html', context)

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ContHist(request):
	roles = get_roles(request)
	read = read_cont_hist()
	objects = []
	for i in read['objects']:
		objects.append(i)
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Projetu nebe Kompleta Ona', 'legend': 'Lista Projetu nebe Kompleta Ona'
	}
	return render(request, 'project/cont_list.html', context)
