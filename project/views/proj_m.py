from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from custom.models import Year
from project.models import PortalHome, ProjMopCat, ProjCat, ProjCap, ProjSec
from project.read_api import read_portal_home, read_proj_cat, read_proj_cap, read_proj_mopcat, read_proj_sec
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def PortalHomeSync(request):
	roles = get_roles(request)
	read = read_portal_home()
	year = read['year']
	data = read['obj']
	obj = PortalHome.objects.first()
	if not obj:
		obj = PortalHome(id=1, year=year, new=data[0], rollover=data[1], completed=data[2],\
		   ongoing=data[3], notstarted=data[4])
		obj.save()
	else:
		obj.year = year
		obj.new = data[0]
		obj.rollover = data[1]
		obj.completed = data[2]
		obj.ongoing = data[3]
		obj.notstarted = data[4]
		obj.save()
	messages.success(request, f'Atualiza ona.')
	return redirect('admin-portal-home')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def PortalHomeEna(request):
	obj = PortalHome.objects.first()
	obj.is_active = True
	obj.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-portal-home')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def PortalHomeDis(request):
	obj = PortalHome.objects.first()
	obj.is_active = False
	obj.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-portal-home')
### MOPCAT
@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMopCatSync(request):
	roles = get_roles(request)
	read = read_proj_mopcat()
	data = read['obj']
	obj = ProjMopCat.objects.first()
	if not obj:
		obj = ProjMopCat(id=1, est=data[0], r4d=data[1], emer=data[2], obrassel=data[3], menor=data[4], bsgsm=data[5])
		obj.save()
	else:
		obj.est = data[0]
		obj.r4d = data[1]
		obj.emer = data[2]
		obj.obrassel = data[3]
		obj.menor = data[4]
		obj.bsgsm = data[5]
		obj.save()
	messages.success(request, f'Atualiza ona.')
	return redirect('admin-proj-mopcat')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMopCatEna(request):
	obj = ProjMopCat.objects.first()
	obj.is_active = True
	obj.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-proj-mopcat')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjMopCatDis(request):
	obj = ProjMopCat.objects.first()
	obj.is_active = False
	obj.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-proj-mopcat')
### CAT
@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjCatSync(request):
	groles = get_roles(request)
	read = read_proj_cat()
	data = read['obj']
	obj = ProjCat.objects.first()
	if not obj:
		obj = ProjCat(id=1, fi=data[0], lm=data[1], emer=data[2])
		obj.save()
	else:
		obj.fi = data[0]
		obj.lm = data[1]
		obj.emer = data[2]
		obj.save()
	messages.success(request, f'Atualiza ona.')
	return redirect('admin-proj-cat')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjCatEna(request):
	obj = ProjCat.objects.first()
	obj.is_active = True
	obj.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-proj-cat')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjCatDis(request):
	obj = ProjCat.objects.first()
	obj.is_active = False
	obj.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-proj-cat')
### CAP
@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjCapSync(request):
	roles = get_roles(request)
	read = read_proj_cap()
	data = read['obj']
	obj = ProjCap.objects.first()
	if not obj:
		obj = ProjCap(id=1, bs=data[0], cm=data[1], cd=data[2])
		obj.save()
	else:
		obj.bs = data[0]
		obj.cm = data[1]
		obj.cd = data[2]
		obj.save()
	messages.success(request, f'Atualiza ona.')
	return redirect('admin-proj-cap')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjCapEna(request):
	obj = ProjCap.objects.first()
	obj.is_active = True
	obj.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-proj-cap')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjCapDis(request):
	obj = ProjCap.objects.first()
	obj.is_active = False
	obj.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-proj-cap')
### SEC
@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjSecSync(request):
	roles = get_roles(request)
	read = read_proj_sec()
	data = read['obj']
	obj = ProjSec.objects.first()
	if not obj:
		obj = ProjSec(id=1, estrada=data[0], ponte=data[1], cheias=data[2], urban=data[3], estudu=data[4],\
			asset=data[5])
		obj.save()
	else:
		obj.estrada = data[0]
		obj.ponte = data[1]
		obj.cheias = data[2]
		obj.urban = data[3]
		obj.estudu = data[4]
		obj.asset = data[5]
		obj.save()
	messages.success(request, f'Atualiza ona.')
	return redirect('admin-proj-sec')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjSecEna(request):
	obj = ProjSec.objects.first()
	obj.is_active = True
	obj.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-proj-sec')

@allowed_users(allowed_roles=['portal_admin','portal_dna'])
def ProjSecDis(request):
	obj = ProjSec.objects.first()
	obj.is_active = False
	obj.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-proj-sec')