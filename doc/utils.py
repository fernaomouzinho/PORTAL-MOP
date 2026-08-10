import os, hashlib
import datetime
from pytz import timezone
from uuid import uuid4

now = datetime.datetime.now(timezone("Asia/Dili"))

def getnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
		hashid = hashlib.md5(str(newid).encode())
	else:
		newid = 1
		hashid = hashlib.md5(str(newid).encode())
	return newid, hashid.hexdigest()

def upload_doc(instance, filename):
	year = datetime.datetime.now()
	upload_to = 'other_docs/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}.{}'.format(instance.pk,filename)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def upload_report(instance, filename):
	upload_to = 'reports/'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}.{}'.format(instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)
