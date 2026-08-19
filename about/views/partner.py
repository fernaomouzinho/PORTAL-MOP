import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from about.models import Partner
from about.forms import PartnerForm
from about.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def PartnerList(request):
    roles = get_roles(request)
    objects = Partner.objects.all()
    context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Parceiru', 'legend': 'Lista Parceiru'
	}
    return render(request, 'partner/list.html', context)

@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def PartnerAdd(request):
	if request.method == 'POST':
		newid, new_hashid = getnewid(Partner)
		form = PartnerForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.datetime = datetime.datetime.now()
			instance.hashed = new_hashid
			instance.user = request.user
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-partner-list')
	else: form = PartnerForm()
	context = {
		'form': form,
		'title': 'Aumenta Parceiru', 'legend': 'Aumenta Parceiru'
	}
	return render(request, 'partner/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def PartnerEdit(request, pk):
	objects = get_object_or_404(Partner, pk=pk)
	if request.method == 'POST':
		form = PartnerForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-partner-list')
	else: form = PartnerForm(instance=objects)
	context = {
		'form': form, 'objects': objects,
		'title': 'Altera Parceiru', 'legend': 'Altera Parceiru'
	}
	return render(request, 'partner/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def PartnerRemove(request, pk):
	objects = get_object_or_404(Partner, pk=pk)
	objects.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-partner-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def PartnerEnable(request, pk):
	objects = get_object_or_404(Partner, pk=pk)
	objects.is_active = True
	objects.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-partner-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def PartnerDisable(request, pk):
	objects = get_object_or_404(Partner, pk=pk)
	objects.is_active = False
	objects.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-partner-list')