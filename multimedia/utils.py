import os, hashlib
from uuid import uuid4

def getnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
		hashid = hashlib.md5(str(newid).encode())
	else:
		newid = 1
		hashid = hashlib.md5(str(newid).encode())
	return newid, hashid.hexdigest()

def upload_album(instance, filename):
	upload_to = 'multimedia/{}'.format(instance.pk)
	field = 'album'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk,ext)
	else: 
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def upload_gallery(instance, filename):
	upload_to = 'multimedia/{}'.format(instance.album.id)
	field = 'images'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}_{}.{}'.format(field,instance.album.id,instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def upload_banner(instance, filename):
	upload_to = 'multimedia/'
	field = 'banner'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)