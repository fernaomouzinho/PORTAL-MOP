import hashlib
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from custom.models import DG, Division, Position, Municipality
from .utils import *

class About(models.Model):
	vision_tt = models.TextField(null=True, blank=True)
	mission_tt = models.TextField(null=True, blank=True)
	hist_tt = models.TextField(null=True, blank=True)
	vision_pt = models.TextField(null=True, blank=True)
	mission_pt = models.TextField(null=True, blank=True)
	hist_pt = models.TextField(null=True, blank=True)
	vision_en = models.TextField(null=True, blank=True)
	mission_en = models.TextField(null=True, blank=True)
	hist_en = models.TextField(null=True, blank=True)
	image = models.ImageField(default='default.jpg', upload_to=about, null=True, blank=True)
	org_chart = models.FileField(upload_to=orgchart, null=True, blank=True)
	def __str__(self):
		template = '{0.vision_tt}'
		return template.format(self)

class Structure(models.Model):
	dg = models.ForeignKey(DG, on_delete=models.CASCADE, null=True, blank=True)
	div = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Diresaun")
	pos = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Pojisaun")
	name = models.CharField(max_length=30, null=True, verbose_name="Naran")
	sex = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')], max_length=4, null=True, blank=True, verbose_name="Sexu")
	desc = models.TextField(null=True, blank=True)
	image = models.ImageField(default='person.jpg', upload_to='orgchart/', null=True, verbose_name="Imajen")
	order = models.IntegerField(null=True, blank=True)
	is_active = models.BooleanField(default=True, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	datetime = models.DateTimeField(null=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class Contact(models.Model):
	email = models.CharField(max_length=30, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	address = models.CharField(max_length=50, null=True, blank=True)
	def __str__(self):
		template = '{0.email}'
		return template.format(self)

class ContactMun(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	mun = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Municipiu")
	email = models.CharField(max_length=30, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	address = models.CharField(max_length=50, null=True, blank=True)
	location = models.CharField(max_length=200, null=True, blank=True)
	lat = models.CharField(max_length=20, null=True, blank=True)
	lng = models.CharField(max_length=20, null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)
###
class Partner(models.Model):
	code = models.CharField(max_length=20, null=True, blank=True)
	name = models.CharField(max_length=300, null=True)
	website = models.CharField(max_length=100, null=True, blank=True)
	image = models.ImageField(upload_to=upload_partner,
			validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
	is_active = models.BooleanField(default=False, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)
