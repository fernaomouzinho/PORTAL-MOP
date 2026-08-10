from django.db import models

class Year(models.Model):
	year = models.IntegerField()
	def __str__(self):
		template = '{0.year}'
		return template.format(self)

class DG(models.Model):
	code = models.CharField(max_length=20)
	name_tt = models.CharField(max_length=100, null=True, blank=True)
	name_pt = models.CharField(max_length=100, null=True, blank=True)
	name_en = models.CharField(max_length=100, null=True, blank=True)
	desc_tt = models.TextField(null=True, blank=True)
	desc_pt = models.TextField(null=True, blank=True)
	desc_en = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='orgchart/', null=True, blank=True, verbose_name="Organograma")
	def __str__(self):
		template = '{0.code} , {0.name_tt}'
		return template.format(self)

class Division(models.Model):
	code = models.CharField(max_length=20)
	name_tt = models.CharField(max_length=100, null=True, blank=True)
	name_pt = models.CharField(max_length=100, null=True, blank=True)
	name_en = models.CharField(max_length=100, null=True, blank=True)
	desc_tt = models.TextField(null=True, blank=True)
	desc_pt = models.TextField(null=True, blank=True)
	desc_en = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='orgchart/', null=True, blank=True, verbose_name="Organograma")
	def __str__(self):
		template = '{0.code} , {0.name_tt}'
		return template.format(self)

class OtherDiv(models.Model):
	code = models.CharField(max_length=20)
	name_tt = models.CharField(max_length=100, null=True, blank=True)
	name_pt = models.CharField(max_length=100, null=True, blank=True)
	name_en = models.CharField(max_length=100, null=True, blank=True)
	desc_tt = models.TextField(null=True, blank=True)
	desc_pt = models.TextField(null=True, blank=True)
	desc_en = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='others/', null=True, blank=True, verbose_name="Upload Logo")
	def __str__(self):
		template = '{0.code} , {0.name_tt}'
		return template.format(self)

class Position(models.Model):
	name_tt = models.CharField(max_length=100, null=True, blank=True)
	name_pt = models.CharField(max_length=100, null=True, blank=True)
	name_en = models.CharField(max_length=100, null=True, blank=True)
	def __str__(self):
		template = '{0.name_tt}'
		return template.format(self)

class Municipality(models.Model):
	code = models.CharField(max_length=5, null=True)
	name = models.CharField(max_length=20, null=True)
	hckey = models.CharField(max_length=10, null=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class AdministrativePost(models.Model):
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=50)
	def __str__(self):
		template = '{0.municipality} - {0.name}'
		return template.format(self)

class Village(models.Model):
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=50)
	def __str__(self):
		template = '{0.administrativepost} - {0.name}'
		return template.format(self)
