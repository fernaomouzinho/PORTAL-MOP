import os
import datetime
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pub.models import Tender
from pub.forms import TenderForm
from pub.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def TenderList(request):
	roles = get_roles(request)
	objects = Tender.objects.all().order_by('-id')
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Tender', 'legend': 'Lista Tender'
	}
	return render(request, 'tender/list.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def TenderAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, new_hashid = getnewid(Tender)
		form = TenderForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-tender-list')
	else: form = TenderForm()
	context = {
	    'group':roles, 'form': form,
		'title': 'Aumenta Tender', 'legend': 'Aumenta Tender'
	}
	return render(request, 'tender/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def TenderEdit(request, hashid):
	roles = get_roles(request)
	objects = get_object_or_404(Tender, hashed=hashid)
	if request.method == 'POST':
		form = TenderForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-tender-det', hashid=hashid)
	else: form = TenderForm(instance=objects)
	context = {
		'group': roles, 'objects': objects, 'form': form,
		'title': 'Altera Tender', 'legend': 'Altera Tender'
	}
	return render(request, 'tender/form.html', context)

@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def TenderDetail(request, hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(Tender, hashed=hashid)
	context = {
		'group': group, 'objects': objects,
		'title': 'Detalha Tender', 'legend': 'Detalha Tender'
	}
	return render(request, 'tender/detail.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def TenderEnable(request, pk):
	objects = get_object_or_404(Tender, pk=pk)
	objects.is_active = True
	objects.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-tender-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def TenderDisable(request, hashid):
	objects = get_object_or_404(Tender, hashed=hashid)
	objects.is_active = False
	objects.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-tender-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_dna'])
def TenderRem(request, pk):
	objects = get_object_or_404(Tender, pk=pk)
	objects.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-tender-list')

def TenderPDF(request, hashid):
	objects = get_object_or_404(Tender, hashed=hashid)
	context = {
		'objects': objects,
		'title': 'Hare PDF',
	}
	return render(request, 'tender/pdf.html', context)

def TenderDownload(request, hashid):
	obj = get_object_or_404(Tender, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response