import datetime
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from doc.models import Report
from doc.forms import ReportForm
from doc.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def ReportList(request):
	roles = get_roles(request)
	objects = Report.objects.all().order_by('-id')
	context = {
		'group': roles, 'objects': objects,
		'title': 'Lista Relatoriu', 'legend': 'Lista Relatoriu'
	}
	return render(request, 'report/list.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def ReportAdd(request):
	roles = get_roles(request)
	if request.method == 'POST':
		newid, new_hashid = getnewid(Report)
		form = ReportForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.user = request.user
			instance.datetime = datetime.datetime.now()
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-report-list')
	else: form = ReportForm()
	context = {
	    'group':roles, 'form': form,
		'title': 'Aumenta Relatoriu', 'legend': 'Aumenta Relatoriu'
	}
	return render(request, 'report/form.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def ReportEdit(request, hashid):
	roles = get_roles(request)
	objects = get_object_or_404(Report, hashed=hashid)
	if request.method == 'POST':
		form = ReportForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-report-det', hashid=hashid)
	else: form = ReportForm(instance=objects)
	context = {
		'group': roles, 'objects': objects, 'form': form,
		'title': 'Altera Relatoriu', 'legend': 'Altera Relatoriu'
	}
	return render(request, 'report/form.html', context)

@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def ReportDetail(request, hashid):
	roles = get_roles(request)
	objects = get_object_or_404(Report, hashed=hashid)
	context = {
		'group': roles, 'objects': objects,
		'title': 'Detalha Relatoriu', 'legend': 'Detalha Relatoriu'
	}
	return render(request, 'report/detail.html', context)


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def ReportEnable(request, pk):
	objects = get_object_or_404(Report, pk=pk)
	objects.is_active = True
	objects.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-report-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def ReportDisable(request, pk):
	objects = get_object_or_404(Report, pk=pk)
	objects.is_active = False
	objects.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-report-list')


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media'])
def ReportRem(request, pk):
	objects = get_object_or_404(Report, pk=pk)
	objects.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-report-list')

def ReportPDF(request, hashid):
	objects = get_object_or_404(Report, hashed=hashid)
	context = {
		'objects': objects,
		'title': 'Hare PDF',
	}
	return render(request, 'report/pdf.html', context)

def ReportDownload(request, hashid):
	obj = get_object_or_404(Report, hashed=hashid)
	filename = str(settings.BASE_DIR)+str(obj.file.url)
	response = FileResponse(open(filename, 'rb'))
	return response