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

def upload_proj_map(instance, filename):
	upload_to = 'proj_map_data/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(instance.datetime,instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)
