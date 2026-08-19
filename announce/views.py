import os
import datetime
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Announce
from .forms import AnnounceForm
from .utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def AnnounceList(request):
	roles = get_roles(request)
	if roles == "portal_admin":
		objects = Announce.objects.all().order_by('-datetime')
	else:
		objects = Announce.objects.filter(user=request.user).all().order_by('-datetime')
	context = {
		'group': roles, 'objects': objects,
		'title': 'Anunciu', 'legend': 'Anunciu'
	}
	return render(request, 'announce/list.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def AnnounceAdd(request):
	if request.method == 'POST':
		newid, new_hashid = getnewid(Announce)
		form = AnnounceForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona')
			return redirect('admin-ann-list')
	else: form = AnnounceForm()
	context = {
		'form': form,
		'title': 'Aumenta Anunciu', 'legend': 'Aumenta Anunciu'
	}
	return render(request, 'announce/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def AnnounceEdit(request, hashid):
	objects = get_object_or_404(Announce, hashed=hashid)
	if request.method == 'POST':
		form = AnnounceForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-ann-det', hashid=hashid)
	else: form = AnnounceForm(instance=objects)
	context = {
		'form': form,
		'title': 'Altera Anunciu', 'legend': 'Altera Anunciu'
	}
	return render(request, 'announce/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def AnnounceDetail(request, hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(Announce, hashed=hashid)
	context = {
		'group': group, 'objects': objects,
		'title': 'Detalha Anunsiu', 'legend': 'Detalha Anunsiu'
	}
	return render(request, 'announce/detail.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def AnnounceEnable(request, pk):
	objects = get_object_or_404(Announce, pk=pk)
	if request.method == 'GET':
		objects.is_active = True
		objects.save()
		messages.success(request, f'Ativa.')
		return redirect('admin-ann-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def AnnounceDisable(request, pk):
	objects = get_object_or_404(Announce, pk=pk)
	if request.method == 'GET':
		objects.is_active = False
		objects.save()
		messages.success(request, f'Desativa.')
		return redirect('admin-ann-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def AnnounceRem(request, pk):
	objects = get_object_or_404(Announce, pk=pk)
	objects.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-ann-list')

def AnnouncePDF(request, hashid):
	objects = get_object_or_404(Announce, hashed=hashid)
	context = {
		'objects': objects,
		'title': 'Hare PDF',
	}
	return render(request, 'announce/pdf.html', context)
##