import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from project.models import ProjMapG, ProjMapS, ProjMapP
from project.forms import ProjMapGForm, ProjMapSForm, ProjMapPForm
from project.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapGAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, _ = getnewid(ProjMapG)
		form = ProjMapGForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-map-g-list')
	else: form = ProjMapGForm()
	context = {
		'group':roles, 'form': form, 'page': 'mapg',
		'title': 'Aumenta Dados Mapa', 'legend': 'Aumenta Dados Mapa'
	}
	return render(request, 'project_map/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapGEdit(request, pk):
	roles = get_roles(request)
	obj = get_object_or_404(ProjMapG, pk=pk)
	if request.method == 'POST':
		form = ProjMapGForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-map-g-list')
	else: form = ProjMapGForm(instance=obj)
	context = {
		'group':roles, 'form': form, 'page': 'mapg',
		'title': 'Altera Dados Mapa', 'legend': 'Altera Dados Mapa'
	}
	return render(request, 'project_map/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapGRem(request, pk):
	obj = get_object_or_404(ProjMapG, pk=pk)
	obj.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-map-g-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapGEna(request, pk):
	obj = get_object_or_404(ProjMapG, pk=pk)
	obj.is_active = True
	obj.save()
	obj2 = ProjMapG.objects.exclude(pk=pk).all()
	for i in obj2:
		i.is_active = False
		i.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-map-g-list')
#

@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapSAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, _ = getnewid(ProjMapS)
		form = ProjMapSForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-map-s-list')
	else: form = ProjMapSForm()
	context = {
		'group':roles, 'form': form, 'page': 'maps',
		'title': 'Aumenta Dados Mapa', 'legend': 'Aumenta Dados Mapa'
	}
	return render(request, 'project_map/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapSEdit(request, pk):
	roles = get_roles(request)
	obj = get_object_or_404(ProjMapS, pk=pk)
	if request.method == 'POST':
		form = ProjMapSForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-map-s-list')
	else: form = ProjMapSForm(instance=obj)
	context = {
		'group':roles, 'form': form, 'page': 'maps',
		'title': 'Altera Dados Mapa', 'legend': 'Altera Dados Mapa'
	}
	return render(request, 'project_map/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapSRem(request, pk):
	obj = get_object_or_404(ProjMapG, pk=pk)
	obj.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-map-s-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapSEna(request, pk):
	obj = get_object_or_404(ProjMapS, pk=pk)
	obj.is_active = True
	obj.save()
	obj2 = ProjMapS.objects.exclude(pk=pk).all()
	for i in obj2:
		i.is_active = False
		i.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-map-s-list')

#

@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapPAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, _ = getnewid(ProjMapP)
		form = ProjMapPForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-map-p-list')
	else: form = ProjMapPForm()
	context = {
		'group':roles, 'form': form, 'page': 'mapp',
		'title': 'Aumenta Dados Mapa', 'legend': 'Aumenta Dados Mapa'
	}
	return render(request, 'project_map/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapPEdit(request, pk):
	roles = get_roles(request)
	obj = get_object_or_404(ProjMapP, pk=pk)
	if request.method == 'POST':
		form = ProjMapPForm(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-map-p-list')
	else: form = ProjMapPForm(instance=obj)
	context = {
		'group':roles, 'form': form, 'page': 'mapp',
		'title': 'Altera Dados Mapa', 'legend': 'Altera Dados Mapa'
	}
	return render(request, 'project_map/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapPRem(request, pk):
	obj = get_object_or_404(ProjMapP, pk=pk)
	obj.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-map-p-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def ProjMapPEna(request, pk):
	obj = get_object_or_404(ProjMapP, pk=pk)
	obj.is_active = True
	obj.save()
	obj2 = ProjMapP.objects.exclude(pk=pk).all()
	for i in obj2:
		i.is_active = False
		i.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-map-p-list')