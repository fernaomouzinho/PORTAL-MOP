from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from django.contrib import messages
from django.contrib.auth.models import User
from about.models import About, Contact, ContactMun
from about.forms import AboutForm, OrgChartForm, ContactForm, ContactMunForm
from about.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['portal_admin'])
def AboutView(request):
	roles = get_roles(request)
	objects = About.objects.first()
	context = {
		'group': roles, 'objects': objects,
	'title': 'Konaba MOP', 'legend': 'Konaba MOP'
  	}
	return render(request, 'about/about.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def AboutEdit(request):
	objects = About.objects.first()
	if request.method == 'POST':
		form = AboutForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-about')
	else: form = AboutForm(instance=objects)
	context = {
		'form': form, 'page': 'about',
		'title': 'Altera', 'legend': 'Altera'
	}
	return render(request, 'about/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def OrgChartEdit(request):
	objects = About.objects.first()
	if request.method == 'POST':
		form = OrgChartForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-orgchart-pdf')
	else: form = OrgChartForm(instance=objects)
	context = {
		'form': form, 'objects': objects, 'page': 'orgchart',
		'title': 'Altera Organograma', 'legend': 'Altera Organograma'
	}
	return render(request, 'about/form.html', context)

def OrgChartPDF(request):
	objects = About.objects.first()
	context = {
		'objects': objects,
		'title': 'Hare PDF', 'legend': 'Hare PDF'
	}
	return render(request, 'about/pdf.html', context)
#
@allowed_users(allowed_roles=['portal_admin'])
def ContView(request):
	objects = Contact.objects.first()
	if request.method == 'POST':
		form = ContactForm(request.POST, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-cont-view')
	else: form = ContactForm(instance=objects)
	context = {
		'objects': objects, 'form': form, 'page': 'cont',
		'title': 'Kontaktu', 'legend': 'Kontaktu'
	}
	return render(request, 'contact/cont.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def ContMunList(request):
	objects = ContactMun.objects.all()
	context = {
		'objects': objects,
		'title': 'Kontaktu MOP iha Municipiu', 'legend': 'Kontaktu MOP iha Municipiu'
	}
	return render(request, 'contact/cont_mun.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def ContMunAdd(request):
	if request.method == 'POST':
		newid, new_hashid = getnewid(ContactMun)
		form = ContactMunForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-cont-mun-list')
	else: form = ContactMunForm()
	context = {
		'form': form, 'page': 'contmun',
		'title': 'Aumenta Kontaktu', 'legend': 'Aumenta Kontaktu'
	}
	return render(request, 'contact/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def ContMunEdit(request, pk):
	objects =get_object_or_404(ContactMun, pk=pk)
	if request.method == 'POST':
		form = ContactMunForm(request.POST, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-cont-mun-list')
	else: form = ContactMunForm(instance=objects)
	context = {
		'objects': objects, 'form': form, 'page': 'contmun',
		'title': 'Altera Kontaktu', 'legend': 'Altera Kontaktu'
	}
	return render(request, 'contact/form.html', context)
