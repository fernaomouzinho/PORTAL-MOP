import os, datetime, hashlib
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

def upload_vaga(instance, filename):
	upload_to = 'vagancy_data/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}.{}'.format(instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def upload_tender(instance, filename):
	upload_to = 'tender_data/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}.{}'.format(instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def upload_pub(instance, filename):
	upload_to = 'publication_data/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}.{}'.format(instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)
