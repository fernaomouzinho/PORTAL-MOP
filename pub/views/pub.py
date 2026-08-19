import os
import datetime
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pub.models import Publication
from pub.forms import PublicationForm
from pub.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def PubList(request):
	roles = get_roles(request)
	objects = Publication.objects.all().order_by('-id')
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Publikasaun', 'legend': 'Lista Publikasaun'
	}
	return render(request, 'pub/list.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def PubAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, new_hashid = getnewid(Publication)
		form = PublicationForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-pub-list')
	else: form = PublicationForm()
	context = {
	    'group':roles, 'form': form,
		'title': 'Aumenta Publikasaun', 'legend': 'Aumenta Publikasaun'
	}
	return render(request, 'pub/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def PubEdit(request, hashid):
	roles = get_roles(request)
	objects = get_object_or_404(Publication, hashed=hashid)
	if request.method == 'POST':
		form = PublicationForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-pub-det', hashid=hashid)
	else: form = PublicationForm(instance=objects)
	context = {
		'group': roles, 'objects': objects, 'form': form,
		'title': 'Altera Publikasaun', 'legend': 'Altera Publikasaun'
	}
	return render(request, 'pub/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def PubDetail(request, hashid):
	roles = get_roles(request)
	objects = get_object_or_404(Publication, hashed=hashid)
	context = {
		'group': roles, 'objects': objects,
		'title': 'Detalha Publikasaun', 'legend': 'Detalha Publikasaun'
	}
	return render(request, 'pub/detail.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def PubEnable(request, pk):
	objects = get_object_or_404(Publication, pk=pk)
	objects.is_active = True
	objects.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-pub-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def PubDisable(request, hashid):
	objects = get_object_or_404(Publication, hashed=hashid)
	objects.is_active = False
	objects.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-pub-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def PubRem(request, pk):
	objects = get_object_or_404(Publication, pk=pk)
	objects.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-pub-list')

def PubPDF(request, hashid):
	objects = get_object_or_404(Publication, hashed=hashid)
	context = {
		'objects': objects,
		'title': 'Hare PDF',
	}
	return render(request, 'pub/pdf.html', context)

def PubDownload(request, hashid):
	obj = get_object_or_404(Publication, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response