from django.shortcuts import render, redirect, get_object_or_404
from about.utils import getnewid
from custom.forms import DGForm, DivisionForm, OtherDivForm
from users.decorators import allowed_users
from django.contrib import messages
from .models import AdministrativePost, Village, Division, DG, OtherDiv
from users.decorators import allowed_users
from portal.utils import get_roles

def load_posts(request):
	mun_id = request.GET.get('municipality')
	posts = AdministrativePost.objects.filter(municipality_id=mun_id).order_by('name')
	return render(request, 'custom/posts_dropdown.html', {'posts': posts})

def load_villages(request):
	post_id = request.GET.get('post')
	villages = Village.objects.filter(administrativepost_id=post_id).order_by('name')
	return render(request, 'custom/villages_dropdown.html', {'villages': villages})
###
@allowed_users(allowed_roles=['portal_admin'])
def DGList(request):
	roles = get_roles(request)
	objects = DG.objects.all().order_by('id')
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Diresaun Geral', 'legend': 'Lista Diresaun Geral'
	}
	return render(request, 'custom/dg_list.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DGAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, _ = getnewid(DG)
		form = DGForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-dg-list')
	else: form = DGForm()
	context = {
		'group': roles, 'form': form, 'page': 'dg',
		'title': 'Aumenta DG', 'legend': 'Aumenta DG'
	}
	return render(request, 'custom/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DGEdit(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(DG, pk=pk)
	if request.method == 'POST':
		form = DGForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-dg-det', pk=pk)
	else: form = DGForm(instance=objects)
	context = {
		'group': roles, 'objects': objects, 'form': form, 'page': 'dg',
		'title': 'Altera DG', 'legend': 'Altera DG'
	}
	return render(request, 'custom/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DGDet(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(DG, pk=pk)
	context = {
		'group': roles, 'objects': objects,
		'title': 'Detalha Diresaun Geral', 'legend': 'Detalha Diresaun Geral'
	}
	return render(request, 'custom/dg_det.html', context)
###
@allowed_users(allowed_roles=['portal_admin'])
def DivList(request):
	roles = get_roles(request)
	objects = Division.objects.all().order_by('id')
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Diresaun Nacional', 'legend': 'Lista Diresaun Nacional'
	}
	return render(request, 'custom/div_list.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DivAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, _ = getnewid(Division)
		form = DivisionForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-div-list')
	else: form = DivisionForm()
	context = {
		'group': roles, 'form': form, 'page': 'div',
		'title': 'Aumenta Diresaun', 'legend': 'Aumenta Diresaun'
	}
	return render(request, 'custom/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DivEdit(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(Division, pk=pk)
	if request.method == 'POST':
		form = DivisionForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-div-det', pk=pk)
	else: form = DivisionForm(instance=objects)
	context = {
		'group': roles, 'objects': objects, 'form': form, 'page': 'div',
		'title': 'Altera Diresaun', 'legend': 'Altera Diresaun'
	}
	return render(request, 'custom/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DivDet(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(Division, pk=pk)
	context = {
		'group': roles, 'objects': objects,
		'title': 'Detalha Diresaun', 'legend': 'Detalha Diresaun'
	}
	return render(request, 'custom/div_det.html', context)
###
@allowed_users(allowed_roles=['portal_admin'])
def OtDivList(request):
	roles = get_roles(request)
	objects = OtherDiv.objects.all().order_by('id')
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Instituisaun Tutela', 'legend': 'Lista Instituisaun Tutela'
	}
	return render(request, 'custom/otdiv_list.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def OtDivAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, _ = getnewid(OtherDiv)
		form = OtherDivForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-otdiv-list')
	else: form = OtherDivForm()
	context = {
		'group': roles, 'form': form, 'page': 'otdiv',
		'title': 'Aumenta Instituisaun Tutela', 'legend': 'Aumenta Instituisaun Tutela'
	}
	return render(request, 'custom/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def OtDivEdit(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(OtherDiv, pk=pk)
	if request.method == 'POST':
		form = OtherDivForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-otdiv-det', pk=pk)
	else: form = OtherDivForm(instance=objects)
	context = {
		'group': roles, 'objects': objects, 'form': form, 'page': 'div',
		'title': 'Altera Instituisaun Tutela', 'legend': 'Altera Instituisaun Tutela'
	}
	return render(request, 'custom/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def OtDivDet(request, pk):
	roles = get_roles(request)
	objects = get_object_or_404(OtherDiv, pk=pk)
	context = {
		'group': roles, 'objects': objects,
		'title': 'Detalha Instituisaun Tutela', 'legend': 'Detalha Instituisaun Tutela'
	}
	return render(request, 'custom/otdiv_det.html', context)
