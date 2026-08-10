import datetime
from django.shortcuts import render, redirect, get_object_or_404
from users.decorators import allowed_users
from django.contrib import messages
from about.models import Structure
from about.forms import StructureForm
from about.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles

@allowed_users(allowed_roles=['portal_admin'])
def StrucList(request):
	roles = get_roles(request)
	objects = Structure.objects.all()
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Estrutura', 'legend': 'Lista Estrutura'
	}
	return render(request, 'struc/list.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def StrucDetail(request, pk):
	roles = get_roles(request)
	struc = get_object_or_404(Structure, pk=pk)
	context = {
        'group': roles, 
		'struc': struc,
		'title': 'Detalla', 'legend': 'Detalha'
	}
	return render(request, 'struc/detail.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def StrucImg(request):
	roles = get_roles(request)
	objects1 = Structure.objects.filter(order=1).all()
	objects2 = Structure.objects.filter(order=2).all()
	objects3 = Structure.objects.filter(order=3).all()
	context = {
        'group': roles, 
		'objects1': objects1, 'objects2': objects2, 'objects3': objects3,
		'title': 'Estrutura', 'legend': 'Estrutura'
	}
	return render(request, 'struc/img.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def StrucAdd(request):
	if request.method == 'POST':
		newid, new_hashid = getnewid(Structure)
		form = StructureForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.datetime = datetime.datetime.now()
			instance.hashed = new_hashid
			instance.user = request.user
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-struc-list')
	else: form = StructureForm()
	context = {
		'form': form,
		'title': 'Aumenta Estrutura', 'legend': 'Aumenta Estrutura'
	}
	return render(request, 'struc/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def StrucEdit(request, pk):
	objects = get_object_or_404(Structure, pk=pk)
	if request.method == 'POST':
		form = StructureForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-struc-list')
	else: form = StructureForm(instance=objects)
	context = {
		'form': form, 'objects': objects,
		'title': 'Altera Estrutura', 'legend': 'Altera Estrutura'
	}
	return render(request, 'struc/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def StrucEna(request, pk):
	objects = get_object_or_404(Structure, pk=pk)
	objects.is_active = True
	objects.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-struc-list')

@allowed_users(allowed_roles=['portal_admin'])
def StrucDis(request, pk):
	objects = get_object_or_404(Structure, pk=pk)
	objects.is_active = False
	objects.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-struc-list')
	