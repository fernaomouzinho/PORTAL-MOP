import hashlib
from django.utils import timezone
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from news.utils import upload_img
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify

class NewsCat(models.Model):
    name_tt = models.CharField(max_length=50, null=True, blank=True)
    name_pt = models.CharField(max_length=50,null=True, blank=True)
    name_en = models.CharField(max_length=50, null=True, blank=True)
    slug_name_tt = models.SlugField(unique=True, blank=True, null=True)  
    slug_name_pt = models.SlugField(unique=True, blank=True, null=True)  
    slug_name_en= models.SlugField(unique=True, blank=True, null=True)  
    
    def save(self, *args, **kwargs):
        # Auto-generate slugs based on the names
        if not self.slug_name_tt and self.name_tt:
            self.slug_name_tt = slugify(self.name_tt)
        if not self.slug_name_pt and self.name_pt:
            self.slug_name_pt = slugify(self.name_pt)
        if not self.slug_name_en and self.name_en:
            self.slug_name_en = slugify(self.name_en)
        
        super().save(*args, **kwargs)

    def __str__(self):
        template = '{0.name_tt}'
        return template.format(self)

class News(models.Model):
    #language = models.CharField(choices=[('Tetum', 'Tetum'), ('Portugues', 'Portugues'), ('English', 'English')], max_length=10, null=True, verbose_name="Lingua")
    cat = models.ForeignKey(NewsCat, on_delete=models.CASCADE, verbose_name="kategoria")
    title_tt = models.CharField(max_length=250, verbose_name="Titulu Nutisia (Tetum)")
    title_pt = models.CharField(max_length=250, null=True, blank=True, verbose_name="Titulu Nutisia (Portugues)")
    title_en = models.CharField(max_length=250, null=True, blank=True, verbose_name="Titulu Nutisia (English)")
    slug_title_tt = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="Titulu Seo (Tetum)")  
    slug_title_pt = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="Titulu Seo (Portugues)")  
    slug_title_en= models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="Titulu Seo (English)")  
    headline_tt = models.TextField(null=True, verbose_name="Sinopsiu Tetum")
    headline_pt = models.TextField(null=True, verbose_name="Sinopsiu Portugues")
    headline_en = models.TextField(null=True, verbose_name="Sinopsiu English")
    content_tt = models.TextField(null=True, blank=True, verbose_name="Konteudu Tetum")
    content_pt = models.TextField(null=True, blank=True, verbose_name="Konteudu Portugues")
    content_en = models.TextField(null=True, blank=True, verbose_name="Konteudu English")
    place = models.CharField(max_length=50, null=True, blank=True, verbose_name="Fatin")
    date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True)
    is_headline = models.BooleanField(default=False, null=True, blank=True)
    is_main = models.BooleanField(default=False, null=True, blank=True)
    hits = models.IntegerField(default=0, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Auto-generate slugs if they are not provided
        if self.title_tt and not self.slug_title_tt:
            self.slug_title_tt = slugify(self.title_tt)
        if self.title_pt and not self.slug_title_pt:
            self.slug_title_pt = slugify(self.title_pt)
        if self.title_en and not self.slug_title_en:
            self.slug_title_en = slugify(self.title_en)

        # Ensure slugs are unique by appending a number if necessary
        self.slug_title_tt = self._generate_unique_slug(self.slug_title_tt)
        self.slug_title_pt = self._generate_unique_slug(self.slug_title_pt)
        self.slug_title_en = self._generate_unique_slug(self.slug_title_en)

        super().save(*args, **kwargs)

    def _generate_unique_slug(self, slug):
        """Generate a unique slug by appending a number if necessary."""
        original_slug = slug
        counter = 1
        while News.objects.filter(slug_title_tt=slug).exists() or News.objects.filter(slug_title_pt=slug).exists() or News.objects.filter(slug_title_en=slug).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        template = '{0.title_tt}'
        return template.format(self)
    

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, related_name="newsimage")
    desc_tt = models.CharField(max_length=200, null=True, blank=True)
    desc_pt = models.CharField(max_length=200, null=True, blank=True)
    desc_en = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    hashed = models.CharField(max_length=32, null=True, blank=True)
    image = ProcessedImageField(upload_to=upload_img, processors=[ResizeToFill(740, 500)],
                                format='JPEG', options={'quality': 60}, null=True, verbose_name="Upload Imajen")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(296, 197)], format='JPEG', options={'quality': 60})
    def __str__(self):
        template = '{0.news.id}:{0.desc_tt}'
        return template.format(self)
