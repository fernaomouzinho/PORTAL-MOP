import hashlib
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from .utils import upload_album, upload_gallery, upload_banner
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class ImageCat(models.Model):
	name_tt = models.CharField(max_length=20, null=True)
	name_pt = models.CharField(max_length=20, null=True, blank=True)
	name_en = models.CharField(max_length=20, null=True, blank=True)
	def __str__(self):
		template = '{0.name_tt}'
		return template.format(self)

class Album(models.Model):
	cat = models.ForeignKey(ImageCat, on_delete=models.CASCADE, null=True, verbose_name="Kategoria")
	desc_tt = models.CharField(max_length=200, null=True, blank=True)
	desc_pt = models.CharField(max_length=200, null=True, blank=True)
	desc_en = models.CharField(max_length=200, null=True, blank=True)
	is_active = models.BooleanField(default=False, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True, blank=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)
	image = models.ImageField(default='default.jpg', upload_to=upload_album, null=True, verbose_name="Upload Imajen")
	image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(250,166)], format='JPEG', options={'quality': 60})
	def __str__(self):
		template = '{0.desc_tt}'
		return template.format(self)

class Gallery(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, related_name="gallery", verbose_name="Album")
	desc_tt = models.CharField(max_length=200, null=True, blank=True)
	desc_pt = models.CharField(max_length=200, null=True, blank=True)
	desc_en = models.CharField(max_length=200, null=True, blank=True)
	is_active = models.BooleanField(default=True)
	image = models.ImageField(default='default.jpg', upload_to=upload_gallery, null=True, verbose_name="Upload Imajen")
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True, blank=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)
	image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(296,197)], format='JPEG', options={'quality': 60})
	def __str__(self):
		template = '{0.album.id} | {0.desc_tt}'
		return template.format(self)

class Banner(models.Model):
	name = models.CharField(max_length=200)
	desc_tt = models.CharField(max_length=200, null=True, blank=True)
	desc_pt = models.CharField(max_length=200, null=True, blank=True)
	desc_en = models.CharField(max_length=200, null=True, blank=True)
	image = models.ImageField(default='banner_default.jpg', upload_to=upload_banner, null=True, verbose_name="Upload Imajen")
	is_active = models.BooleanField(default=False, null=True)
	attr = models.CharField(choices=[('',''),('active','active')], max_length=6, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class Video(models.Model):
	language = models.CharField(choices=[('Tetum','Tetum'),('Portugues','Portugues'),('English','English')], max_length=10, null=True, verbose_name="Lingua")
	source = models.CharField(choices=[('Youtube','Youtube'),('Facebook','Facebook')], max_length=10, null=True, verbose_name="Source")
	title = models.CharField(max_length=200, null=True, blank=True)
	embed_url = models.TextField(null=True, blank=False)
	date = models.DateField(null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	is_main = models.BooleanField(default=False, null=True)
	is_active = models.BooleanField(default=False, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	datetime = models.DateTimeField(null=True)
	hashed = models.CharField(max_length=32, null=True)
	def __str__(self):
		template = '{0.title}'
		return template.format(self)