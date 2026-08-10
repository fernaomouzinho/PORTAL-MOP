import os, datetime, hashlib, re
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

def title_seo(title):
	result = re.sub('[\W_]+', '-', title)
	return result.lower()

def upload_img(instance, filename):
	upload_to = 'news/images/{}/{}/'.format(instance.news.date.year,instance.news.date.month)
	field = 'news'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}_{}.{}'.format(field,instance.news.id,instance.pk,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)

def log_news(path,id,category,title,headline,content,author,image):
	log_data = str(id)+','+str(category)+','+str(title)+','+str(headline)+',\
	'+str(content)+','+str(author)+','+str(image)+','+str(datetime.datetime.now())+';\n'

	with open(path, 'a+') as f:
		f.write(log_data)
		f.close()

def log_newsimage(path,newsid,imageid,description,image):
	log_data = str(newsid)+','+str(imageid)+','+str(description)+','+str(image)+','+str(datetime.datetime.now())+';\n'

	with open(path, 'a+') as f:
		f.write(log_data)
		f.close()
