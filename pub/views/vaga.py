import os
import datetime
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pub.models import Vaga
from pub.forms import VagaForm
from pub.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_hr'])
def VagaList(request):
    roles = get_roles(request)
    objects = Vaga.objects.all().order_by('-id')
    context = {
        'group': roles, 'objects': objects,
        'title': 'Lista Vaga', 'legend': 'Lista Vaga'
    }
    return render(request, 'vaga/list.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_hr'])
def VagaAdd(request):
    roles = get_roles(request)
    if request.method == 'POST':
        newid, new_hashid = getnewid(Vaga)
        form = VagaForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = newid
            instance.user = request.user
            instance.datetime = datetime.datetime.now()
            instance.hashed = new_hashid
            instance.save()
            messages.success(request, f'Aumenta ona.')
            return redirect('admin-vaga-list')
    else: form = VagaForm()
    context = {
        'group':roles, 'form': form,
        'title': 'Aumenta Vaga', 'legend': 'Aumenta Vaga'
    }
    return render(request, 'vaga/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_hr'])
def VagaEdit(request, hashid):
    roles = get_roles(request)
    objects = get_object_or_404(Vaga, hashed=hashid)
    if request.method == 'POST':
        form = VagaForm(request.POST, request.FILES, instance=objects)
        if form.is_valid():
            form.save()
            messages.success(request, f'Altera ona.')
            return redirect('admin-vaga-det', hashid=hashid)
    else: form = VagaForm(instance=objects)
    context = {
        'group': roles, 'objects': objects, 'form': form,
        'title': 'Altera Vaga', 'legend': 'Altera Vaga'
    }
    return render(request, 'vaga/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_hr'])
def VagaDetail(request, hashid):
    roles = get_roles(request)
    objects = get_object_or_404(Vaga, hashed=hashid)
    context = {
        'group': roles, 'objects': objects,
        'title': 'Detalha Vaga', 'legend': 'Detalha Vaga'
    }
    return render(request, 'vaga/detail.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_hr'])
def VagaEnable(request, pk):
    objects = get_object_or_404(Vaga, pk=pk)
    objects.is_active = True
    objects.save()
    messages.success(request, f'Ativa ona.')
    return redirect('admin-vaga-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_hr'])
def VagaDisable(request, pk):
    objects = get_object_or_404(Vaga, pk=pk)
    objects.is_active = False
    objects.save()
    messages.success(request, f'Desativa ona.')
    return redirect('admin-vaga-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_hr'])
def VagaRem(request, pk):
    objects = get_object_or_404(Vaga, pk=pk)
    objects.delete()
    messages.success(request, f'Hapaga ona.')
    return redirect('admin-vaga-list')

def VagaPDF(request, hashid):
    objects = get_object_or_404(Vaga, hashed=hashid)
    context = {
        'objects': objects,
        'title': 'Hare PDF',
    }
    return render(request, 'vaga/pdf.html', context)

def VagaDownload(request, hashid):
    obj = get_object_or_404(Vaga, hashed=hashid)
    filename = str(settings.BASE_DIR)+str(obj.file.url)
    response = FileResponse(open(filename, 'rb'))
    return response