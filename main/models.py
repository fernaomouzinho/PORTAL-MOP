from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Languague(models.Model):
    name= models.CharField(max_length=20, null=True)
    abrev= models.CharField(max_length=2, null=True)
    icon_lang = models.ImageField(upload_to='icon_languagues', null=True, blank=True)

    class Meta:
        verbose_name_plural = _('Icon Lingua')

    def __str__(self):
        return str(self.name)