from django.contrib import admin
from .models import *

admin.site.register(DocType)
admin.site.register(Doc)
admin.site.register(Report)
admin.site.register(ReportOwner)