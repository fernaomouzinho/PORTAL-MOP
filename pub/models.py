from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .utils import upload_pub, upload_vaga, upload_tender
import datetime
from django.utils.text import slugify

class Vaga(models.Model):
    language = models.CharField(choices=[('Tetum', 'Tetum'), ('Portugues', 'Portugues'), (
        'English', 'English')], max_length=10, null=True, verbose_name="Lingua")
    title = models.CharField(max_length=300, null=True)
    date = models.DateField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to=upload_vaga,
            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    image = models.ImageField(upload_to=upload_vaga,
            validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
    is_active = models.BooleanField(default=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.title}'
        return template.format(self)
    
class TenderCategory(models.Model):
    name_en = models.CharField(max_length=100)
    name_tt = models.CharField(max_length=100, blank=True, null=True)
    name_pt = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name_en

class Tender(models.Model):
    language = models.CharField(
        choices=[
            ('Tetum', 'Tetum'),
            ('Portugues', 'Portugues'),
            ('English', 'English')
        ],
        max_length=20,
        null=True
    )

    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True, null=True)

    reference_no = models.CharField(max_length=100, blank=True, null=True)

    short_desc = models.CharField(max_length=300, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    category = models.ForeignKey(TenderCategory, on_delete=models.CASCADE)

    publish_date = models.DateField(blank=True, null=True)
    closing_date = models.DateField(blank=True, null=True)
    opening_date = models.DateField(blank=True, null=True)

    estimated_budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True
    )

    currency = models.CharField(max_length=10, default="USD")

    status = models.CharField(
        max_length=20,
        choices=[
            ('draft','Draft'),
            ('open','Open'),
            ('closed','Closed'),
            ('awarded','Awarded'),
            ('cancelled','Cancelled')
        ],
        default='draft'
    )

    file = models.FileField(upload_to=upload_tender)
    image = models.ImageField(upload_to=upload_tender)

    views = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Auto-generate slugs based on the names
        if not self.slug and self.title:
            self.slug = slugify(self.title)
       
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def ends_within_7_days(self):
        return (datetime.date.today() - self.date).days 

class Publication(models.Model):
    language = models.CharField(choices=[('Tetum', 'Tetum'), ('Portugues', 'Portugues'), (
        'English', 'English')], max_length=10, null=True, verbose_name="Lingua")
    title = models.CharField(max_length=300, null=True)
    desc = models.CharField(max_length=300, null=True)
    file = models.FileField(upload_to=upload_pub,
            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    image = models.ImageField(upload_to=upload_pub,
            validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
    is_active = models.BooleanField(default=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        template = '{0.title}'
        return template.format(self)
