from django.contrib import admin
from . models import Download

# Register your models here.

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")