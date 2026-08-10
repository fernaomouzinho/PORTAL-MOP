import os
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .utils import upload_proj_map

class PortalHome(models.Model):
	year = models.IntegerField(null=True, blank=True)
	new = models.IntegerField(default=0, null=True, blank=True)
	rollover = models.IntegerField(default=0, null=True, blank=True)
	completed = models.IntegerField(default=0, null=True, blank=True)
	ongoing = models.IntegerField(default=0, null=True, blank=True)
	notstarted = models.IntegerField(default=0, null=True, blank=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		template = '{0.new}-{0.rollover}-{0.completed}-{0.ongoing}-{0.notstarted}'
		return template.format(self)
###
class ProjMopCat(models.Model):
	est = models.IntegerField(null=True, blank=True)
	r4d = models.IntegerField(null=True, blank=True)
	emer = models.IntegerField(null=True, blank=True)
	obrassel = models.IntegerField(null=True, blank=True)
	menor = models.IntegerField(null=True, blank=True)
	bsgsm = models.IntegerField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		template = '{0.est} - {0.r4d} - {0.emer} - {0.obrassel} - {0.menor} - {0.bsgsm}'
		return template.format(self)

class ProjCat(models.Model):
	fi = models.IntegerField(null=True, blank=True)
	lm = models.IntegerField(null=True, blank=True)
	emer = models.IntegerField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		template = '{0.fi} - {0.lm} - {0.emer}'
		return template.format(self)

class ProjCap(models.Model):
	bs = models.IntegerField(null=True, blank=True)
	cm = models.IntegerField(null=True, blank=True)
	cd = models.IntegerField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		template = '{0.bs} - {0.cm} - {0.cd}'
		return template.format(self)

class ProjSec(models.Model):
	estrada = models.IntegerField(null=True, blank=True)
	ponte = models.IntegerField(null=True, blank=True)
	cheias = models.IntegerField(null=True, blank=True)
	urban = models.IntegerField(null=True, blank=True)
	estudu = models.IntegerField(null=True, blank=True)
	asset = models.IntegerField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		template = '{0.is_active}'
		return template.format(self)
#
class ProjMapG(models.Model):
	subject = models.CharField(max_length=200, null=True, verbose_name="Titulu")
	file = models.FileField(upload_to=upload_proj_map,
			validators=[FileExtensionValidator(allowed_extensions=['js'])], verbose_name="Upload file .js")
	is_active = models.BooleanField(default=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True)
	def __str__(self):
		template = '{0.subject}'
		return template.format(self)

class ProjMapS(models.Model):
	subject = models.CharField(max_length=200, null=True, verbose_name="Titulu")
	file = models.FileField(upload_to=upload_proj_map,
			validators=[FileExtensionValidator(allowed_extensions=['js'])], verbose_name="Upload file .js")
	is_active = models.BooleanField(default=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True)
	def __str__(self):
		template = '{0.subject}'
		return template.format(self)

class ProjMapP(models.Model):
	subject = models.CharField(max_length=200, null=True, verbose_name="Titulu")
	file = models.FileField(upload_to=upload_proj_map,
			validators=[FileExtensionValidator(allowed_extensions=['js'])], verbose_name="Upload file .js")
	is_active = models.BooleanField(default=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True)
	def __str__(self):
		template = '{0.subject}'
		return template.format(self)