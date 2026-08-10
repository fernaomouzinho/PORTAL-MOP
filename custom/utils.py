import os, datetime, re
from pytz import timezone
import hashlib
from base64 import b64encode, b64decode
from django.conf import settings

now = datetime.datetime.now(timezone("Asia/Dili"))

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
	m = ['Janeiru','Febreiru','Marsu','Abril','Maio','Junu','Jullu','Agostu',
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
	m = ['January','February','March','April','May','June','July','August','September',
		'October','November','December']
	return m[month-1]