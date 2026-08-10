from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .utils import upload

class AnnounceType(models.Model):
	name_tt = models.CharField(max_length=20, null=True, blank=True)
	name_pt = models.CharField(max_length=20, null=True, blank=True)
	name_en = models.CharField(max_length=20, null=True, blank=True)
	def __str__(self):
		template = '{0.name_tt}'
		return template.format(self)

class Announce(models.Model):
	type = models.ForeignKey(AnnounceType, on_delete=models.CASCADE, null=True, verbose_name="Tipu")
	language = models.CharField(choices=[('Tetum','Tetum'),('Portugues','Portugues'),('English','English')], max_length=10, null=True, verbose_name="Lingua")
	title = models.CharField(max_length=300)
	date = models.DateField(null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	file = models.FileField(upload_to=upload,
            validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="PDF")
	image = models.ImageField(default='default.jpg', upload_to=upload, null=True, blank=True)
	is_active = models.BooleanField(default=True, null=True)
	datetime = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)
	def __str__(self):
		template = '{0.title}'
		return template.format(self)