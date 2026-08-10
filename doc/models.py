from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .utils import upload_doc, upload_report

class DocType(models.Model):
	name_tt = models.CharField(max_length=20, null=True, blank=True)
	name_pt = models.CharField(max_length=20, null=True, blank=True)
	name_en = models.CharField(max_length=20, null=True, blank=True)
	def __str__(self):
		template = '{0.name_tt}'
		return template.format(self)

class Doc(models.Model):
	doc_type = models.ForeignKey(DocType, on_delete=models.CASCADE, null=True, verbose_name="Tipu Dokumentu")
	language = models.CharField(choices=[('Tetum','Tetum'),('Portugues','Portugues'),('English','English')], max_length=10, null=True, verbose_name="Lingua")
	title = models.CharField(max_length=300, null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	file = models.FileField(upload_to=upload_doc,
			validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name="PDF")
	is_active = models.BooleanField(default=True, null=True)
	datetime = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)
	def __str__(self):
		template = '{0.title}'
		return template.format(self)

class ReportOwner(models.Model):
	code = models.CharField(max_length=10, null=True, blank=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	def __str__(self):
		template = '{0.code}'
		return template.format(self)

class Report(models.Model):
	owner = models.ForeignKey(ReportOwner, on_delete=models.CASCADE, null=True)
	language = models.CharField(choices=[('Tetum', 'Tetum'), ('Portugues', 'Portugues'), (
		'English', 'English')], max_length=10, null=True, verbose_name="Lingua")
	title = models.CharField(max_length=300, null=True)
	date = models.DateField(null=True, blank=True)
	desc = models.TextField(null=True, blank=True)
	file = models.FileField(upload_to=upload_report,
			validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	image = models.ImageField(upload_to=upload_report,
			validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
	is_active = models.BooleanField(default=False, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	datetime = models.DateTimeField(null=True, blank=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)
	def __str__(self):
		template = '{0.title}'
		return template.format(self)
