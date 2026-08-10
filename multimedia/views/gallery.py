import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from django.contrib import messages
from django.core.paginator import Paginator
from multimedia.models import Album, Gallery
from multimedia.forms import AlbumForm, GalleryForm
from multimedia.utils import getnewid
from users.decorators import allowed_users
from portal.utils import get_roles


@allowed_users(allowed_roles=['portal_admin'])
def AlbumList(request):
	group = request.user.groups.all()[0].name
	objects = []
	objects = Album.objects.all().order_by('-datetime')
	paginator = Paginator(objects,4)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
		'objects': objects, 'page_obj':page_obj, 
		'title': 'Album', 'legend': 'Album'
	}
	return render(request, 'mul_gallery/album_list.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def AlbumAdd(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		newid, new_hashid = getnewid(Album)
		form = AlbumForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.datetime = datetime.datetime.now()
			instance.user = request.user
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-album-list')
	else: form = AlbumForm()
	context = {
		'form': form, 'page': 'album',
		'title': 'Aumenta Album', 'legend': 'Aumenta Album'
	}
	return render(request, 'mul_gallery/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def AlbumUpdate(request, hashid):
	group = request.user.groups.all()[0].name
	album = get_object_or_404(Album, hashed=hashid)
	if request.method == 'POST':
		form = AlbumForm(request.POST, request.FILES, instance=album)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-album-list')
	else: form = AlbumForm(instance=album)
	context = {
		'form': form, 'page': 'album',
		'title': 'Update Album', 'legend': 'Update Album'
	}
	return render(request, 'mul_gallery/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def AlbumRemove(request, pk):
	objects = get_object_or_404(Album, pk=pk)
	objects.delete()
	messages.success(request, f'Hapaga ona.')
	return redirect('admin-album-list')

@allowed_users(allowed_roles=['portal_admin'])
def AlbumEnable(request, pk):
	objects = get_object_or_404(Album, pk=pk)
	objects.is_active = True
	objects.save()
	messages.success(request, f'Ativa')
	return redirect('admin-album-list')

@allowed_users(allowed_roles=['portal_admin'])
def AlbumDisable(request, pk):
	objects = get_object_or_404(Album, pk=pk)
	objects.is_active = False
	objects.save()
	messages.success(request, f'Desativa')
	return redirect('admin-album-list')
#gallery
@allowed_users(allowed_roles=['portal_admin'])
def GalleryList(request, hashid):
	group = request.user.groups.all()[0].name
	album = get_object_or_404(Album, hashed=hashid)
	objects = Gallery.objects.filter(album=album).all()
	context = {
		'group': group, 'album': album, 'objects': objects,
		'title': 'Imajen', 'legend': 'Imajen', 
	}
	return render(request, 'mul_gallery/gallery_list.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def GalleryAdd(request, hashid):
	album = get_object_or_404(Album, hashed=hashid)
	if request.method == 'POST':
		newid, new_hashid = getnewid(Gallery)
		form = GalleryForm(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.album = album
			instance.datetime = datetime.datetime.now()
			instance.user = request.user
			instance.hashed = new_hashid
			instance.save()
			messages.success(request, f'Aumenta ona.')
			return redirect('admin-gallery-list', hashid=hashid)
	else: form = GalleryForm()
	context = {
		'album': album, 'form': form,
		'title': 'Aumenta Imajen', 'legend': 'Aumenta Imajen'
	}
	return render(request, 'mul_gallery/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def GalleryEdit(request, hashid, hashid2):
	album = get_object_or_404(Album, hashed=hashid)
	objects = get_object_or_404(Gallery, hashed=hashid2)
	if request.method == 'POST':
		form = GalleryForm(request.POST, request.FILES, instance=objects)
		if form.is_valid():
			form.save()
			messages.success(request, f'Altera ona.')
			return redirect('admin-gallery-list', hashid=hashid)
	else: form = GalleryForm(instance=objects)
	context = {
		'album': album, 'objects': objects, 'form': form,
		'title': 'Altera Imajen', 'legend': 'Altera Imajen'
	}
	return render(request, 'mul_gallery/form.html', context)

@allowed_users(allowed_roles=['portal_admin'])
def GalleryRemove(request, hashid, pk):
	gallery = get_object_or_404(Gallery, pk=pk)
	if request.method == 'GET':
		gallery.delete()
		messages.success(request, f'Hapaga ona.')
		return redirect('admin-gallery-list', hashid=hashid)

@allowed_users(allowed_roles=['portal_admin'])
def GalleryEnable(request, hashid, pk):
	gallery = get_object_or_404(Gallery, pk=pk)
	if request.method == 'GET':
		gallery.is_active = True
		gallery.save()
		messages.success(request, f'Ativa ona.')
		return redirect('admin-gallery-list', hashid=hashid)

@allowed_users(allowed_roles=['portal_admin'])
def GalleryDisable(request, hashid, pk):
	gallery = get_object_or_404(Gallery, pk=pk)
	if request.method == 'GET':
		gallery.is_active = False
		gallery.save()
		messages.success(request, f'Desativa ona.')
		return redirect('admin-gallery-list', hashid=hashid)
