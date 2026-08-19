import os
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from multimedia.models import Banner
from multimedia.forms import BannerForm
from multimedia.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def BannerList(request):
	objects = Banner.objects.all()
	context = {
		'objects': objects,
		'title': 'Banner', 'legend': 'Banner'
	}
	return render(request, 'mul_banner/list.html', context)



@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def BannerAdd(request):
	if request.method == 'POST':
		newid, new_hashid = getnewid(Banner)
		form = BannerForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = new_hashid
			instance.datetime = datetime.datetime.now()
			instance.user = request.user
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-banner-list')
	else: form = BannerForm()
	context = {
		'form': form,
		'title': 'Aumenta Banner', 'legend': 'Aumenta Banner'
	}
	return render(request, 'mul_banner/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def BannerEdit(request, pk):
	objects = get_object_or_404(Banner, pk=pk)
	if request.method == 'POST':
		form = BannerForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-banner-list')
	else: form = BannerForm(instance=objects)
	context = {
		'objects': objects,'form': form,
		'title': 'Altera Banner', 'legend': 'Altera Banner'
	}
	return render(request, 'mul_banner/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def BannerRem(request, pk):
	banner = get_object_or_404(Banner, pk=pk)
	if request.method == 'GET':
		banner.delete()
		messages.success(request, f'Hapaga ona.')
		return redirect('admin-banner-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def BannerEnable(request, pk):
	objects = get_object_or_404(Banner, pk=pk)
	objects.is_active = True
	objects.attr = ""
	objects.save()
	# objects2 = Banner.objects.exclude(hashed=hashid)
	# for i in objects2:
		# i.is_active = False
		# i.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-banner-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def BannerDisable(request, pk):
	objects = get_object_or_404(Banner, pk=pk)
	objects.is_active = False
	objects.attr = ""
	objects.save()
	# objects2 = Banner.objects.exclude(hashed=hashid)
	# for i in objects2:
		# i.is_active = False
		# i.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-banner-list')
