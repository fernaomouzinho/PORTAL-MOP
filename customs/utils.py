import os, datetime, re
from pytz import timezone
import hashlib
from base64 import b64encode, b64decode
from django.conf import settings

now = datetime.datetime.now(timezone("Asia/Dili"))

def getlastid(table_name):
	result = table_name.objects.last()
	if result:
		lastid = result.id
		newid = lastid + 1
	else:
		lastid = 0
		newid = 1
	return newid

def hash_md5(strhash):
	hashed = hashlib.md5(strhash.encode())
	return hashed.hexdigest()

def save_picture(form_picture):
	image_parts = form_picture.split(";base64,")
	return image_parts

def read_picture(picture_column):
	image = b64encode(picture_column).decode("utf-8")
	image = image.split("/jpegbase64")
	return image[1]

def base64toImage(imgstring, memberid, date):
	year = date.strftime("%Y")
	month = date.strftime("%m")
	imgdata = b64decode(imgstring)
	filename = str(memberid)+'.jpg'
	if not os.path.exists('media/member_photo/'+year+'/'+month+'/'):
		os.makedirs('media/member_photo/'+year+'/'+month+'/')
	path = settings.MEDIA_ROOT+"/member_photo/"+year+"/"+month+"/"+filename
	with open(path, 'wb') as f:
		f.write(imgdata)

def f_monthname(month):
	m = ['Janeiru','Fevereiru','Marsu','Abril','Maiu','Junu','Jullu','Agostu',
		'Setembru','Outubru','Novembru','Dezembru']
	return m[month-1]

def f_monthname_tet(month):
	m = ['Janeiru','Fevereiru','Marsu','Abril','Maiu','Junu','Jullu','Agostu','Setembru',
		'Outubru','Novembru','Dezembru']
	return m[month-1]

def f_monthname_por(month):
	m = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro',
		'Outubro','Novembro','Desembro']
	return m[month-1]

def f_monthname_eng(month):
	m = ['January','February','March','April','May','June','july','August','September',
		'October','November','Desember']
	return m[month-1]

def month_name_to_number(month_name):
    month_map = {
        'Janeiru': 1, 'Fevereiru': 2, 'Marsu': 3, 'Abril': 4, 'Maiu': 5, 'Junu': 6,
        'Jullu': 7, 'Agostu': 8, 'Setembru': 9, 'Outubru': 10, 'Novembru': 11, 'Dezembru': 12,
		'Janeiro': 1, 'Fevereiro': 2, 'Marco': 3, 'Abril': 4, 'Maio': 5, 'Junho': 6,
        'Julho': 7, 'Agosto': 8, 'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Desembro': 12,
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    month_name = month_name.title()
    return month_map.get(month_name, None)