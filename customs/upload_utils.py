import os
import datetime
from uuid import uuid4
from customs.utils import getlastid

def path_and_rename_about(instance, filename):
	upload_to = 'profile_files'
	field = 'about'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_orgchart(instance, filename):
	upload_to = 'profile_files'
	field = 'orgchart'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)


def path_and_rename_news(instance, filename):
	upload_to = 'news/images/{}/{}/'.format(instance.news.date_posted.year,instance.news.date_posted.month)
	field = 'news'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}_{}.{}'.format(field,instance.news.id,instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_album(instance, filename):
	field = 'album'
	ext = filename.split('.')[-1]
	if instance.pk:
		upload_to = 'gallery_image/{}'.format(instance.pk)
		filename = '{}_{}.{}'.format(field,instance.pk, ext)
	else:
		upload_to = 'gallery_image/{}'.format("1")
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_gallery(instance, filename):
	upload_to = 'gallery_image/{}'.format(instance.album.id)
	field = 'gallery'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}_{}.{}'.format(field,instance.album.id,instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_download(instance, filename):
	year = datetime.datetime.now()
	upload_to = 'download_files/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}.{}'.format(instance.pk,filename)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_annoucement(instance, filename):
	year = datetime.datetime.now()
	upload_to = 'annoucement_files/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}.{}'.format(instance.pk,filename)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_powner(instance, filename):
	upload_to = 'powner_image/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}'.format(instance.pk,filename)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_banner(instance, filename):
	upload_to = 'gallery_image/'
	field = 'banner'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_templates(instance, filename):
	upload_to = 'templates_image/{}'.format(instance.templates.id)
	field = 'templates'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_project(instance, filename):
	upload_to = 'project_data/{}'.format(instance.year)
	field = 'projects'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.project_type,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_project_data(instance, filename):
	upload_to = 'project/{}/{}'.format(instance.year)
	field = 'projects'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.project_type,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def path_and_rename_rnddoc(instance, filename):
	upload_to = 'rnd_files/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(instance.pk,instance.entered_date,filename)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)
