import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from multimedia.models import Video
from multimedia.forms import VideoForm
from multimedia.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def VideoList(request):
	objects = Video.objects.all().order_by('-date','id')
	context = {
		'objects': objects,
		'title': 'Video', 'legend': 'Video'
	}
	return render(request, 'mul_video/list.html', context)

@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def VideoAdd(request):
	if request.method == 'POST':
		newid, new_hashid = getnewid(Video)
		form = VideoForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.datetime = datetime.datetime.now()
			instance.user = request.user
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-video-list')
	else: form = VideoForm()
	context = {
		'form': form,
		'title': 'Aumenta Video', 'legend': 'Aumenta Video'
	}
	return render(request, 'mul_video/form.html', context)

@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def VideoEdit(request, pk):
	objects = get_object_or_404(Video, pk=pk)
	if request.method == 'POST':
		form = VideoForm(request.POST, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-video-list')
	else: form = VideoForm(instance=objects)
	context = {
		'objects': objects,'form': form,
		'title': 'Altera Video', 'legend': 'Altera Video'
	}
	return render(request, 'mul_video/form.html', context)

@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def VideoRemove(request, pk):
	objects = get_object_or_404(Video, pk=pk)
	objects.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-video-list')

@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def VideoEnable(request, pk):
	objects = get_object_or_404(Video, pk=pk)
	objects.is_active = True
	objects.save()
	messages.success(request, f'Ativa ona.')
	return redirect('admin-video-list')

@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def VideoDisable(request, pk):
	objects = get_object_or_404(Video, pk=pk)
	objects.is_active = False
	objects.save()
	messages.success(request, f'Desativa ona.')
	return redirect('admin-video-list')

@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def VideoMain(request, pk):
	objects = get_object_or_404(Video, pk=pk)
	objects2 = Video.objects.exclude(pk=pk).all()
	objects.is_main = True
	objects.save()
	for i in objects2:
		i.is_main = False
		i.save()
	messages.success(request, f'Main okay.')
	return redirect('admin-video-list')

@allowed_users(allowed_roles=['sii_admin','portal_admin'])
def VideoPlay(request, pk):
	objects = get_object_or_404(Video, pk=pk)
	context = {
		'objects': objects,
		'title': 'Hare Video', 'legend': 'Hare Video'
	}
	return render(request, 'mul_video/play.html', context)
