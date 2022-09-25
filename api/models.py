from django.db import models


class ScrapedItem(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(unique=True, max_length=2047, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)