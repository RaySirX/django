from django.contrib import admin
from . import models
# Register your models here.

class SettingsEntryAdmin(admin.ModelAdmin):
    list_display = ("name", "value")
    prepopulated_fields = { "slug":("name",) }

admin.site.register(models.SettingsEntry, SettingsEntryAdmin)
