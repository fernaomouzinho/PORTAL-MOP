from django.contrib import admin
from .models import NewsCat, News, NewsImage

admin.site.register(NewsCat)
admin.site.register(News)
admin.site.register(NewsImage)
