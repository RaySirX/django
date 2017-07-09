from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class SettingsEntry(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Settings Entry"
        verbose_name_plural = "Settings Entries"
        ordering = ["name"]
