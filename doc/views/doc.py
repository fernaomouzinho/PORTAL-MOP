import os
import datetime
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from users.decorators import allowed_users
from django.contrib import messages
from django.contrib.auth.models import User
from doc.models import Doc
from doc.forms import DocForm
from doc.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles

@allowed_users(allowed_roles=['portal_admin'])
def DocList(request):
	roles = get_roles(request)
	objects = Doc.objects.filter().all().order_by('-datetime')
	context = {
		'group': roles, 'objects': objects,
		'title': 'Dokumentu', 'legend': 'Dokumentu'
	}
	return render(request, 'doc/list.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DocAdd(request):
	if request.method == 'POST':
		newid, new_hashid = getnewid(Doc)
		form = DocForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-doc-list')
	else: form = DocForm()
	context = {
		'form': form,
		'title': 'Aumenta Dokumentu', 'legend': 'Aumenta Dokumentu'
	}
	return render(request, 'doc/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DocEdit(request, hashid):
	objects = get_object_or_404(Doc, hashed=hashid)
	if request.method == 'POST':
		form = DocForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-doc-list')
	else: form = DocForm(instance=objects)
	context = {
		'form': form,
		'title': 'Altera Dokumentu', 'legend': 'Altera Dokumentu'
	}
	return render(request, 'doc/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DocDetail(request, hashid):
	roles = get_roles(request)
	doc = get_object_or_404(Doc, hashed=hashid)
	context = {
		'group': roles, 'doc': doc,
		'title': 'Detalha Dokumentu', 'legend': 'Detalha Dokumentu'
	}
	return render(request, 'doc/detail.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def DocEnable(request, pk):
	objects = get_object_or_404(Doc, pk=pk)
	objects.is_active = True
	objects.save()
	messages.success(request, f'Ativa.')
	return redirect('admin-doc-list')

@allowed_users(allowed_roles=['portal_admin'])
def DocDisable(request, pk):
	objects = get_object_or_404(Doc, pk=pk)
	objects.is_active = False
	objects.save()
	messages.success(request, f'Desativa.')
	return redirect('admin-doc-list')

@allowed_users(allowed_roles=['portal_admin'])
def DocRem(request, pk):
	objects = get_object_or_404(Doc, pk=pk)
	objects.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-doc-list')

def DocPDF(request, hashid):
	doc = get_object_or_404(Doc, hashed=hashid)
	context = {
		'doc': doc,
		'title': 'PDF', 'legend': 'PDF'
	}
	return render(request, 'doc/pdf.html', context)