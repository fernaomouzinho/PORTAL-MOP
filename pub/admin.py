from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Publication, TenderCategory, Tender


# PUBLICATION
@admin.register(Publication)
class PublicationAdmin(ImportExportModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    list_filter = ("datetime",)


# TENDER CATEGORY
@admin.register(TenderCategory)
class TenderCategoryAdmin(ImportExportModelAdmin):
    list_display = ("id", "name_en", "code")
    search_fields = ("name_en", "code")


# TENDER
@admin.register(Tender)
class TenderAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "category", "status", "datetime")
    list_filter = ("status", "category")
    search_fields = ("title",)