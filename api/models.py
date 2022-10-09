from django.db import models


class ScrapedItem(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(unique=True, max_length=2047, blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False)
    last_seen = models.DateTimeField(blank=False, null=False)

# TODO: Should these two be combined to save a filter step?
class WantItem(models.Model):
    item_id = models.ForeignKey(ScrapedItem, on_delete=models.CASCADE, default=None)
    judge_date = models.DateTimeField(blank=False, null=False, auto_now_add=True)

class IgnoreItem(models.Model):
    item_id = models.ForeignKey(ScrapedItem, on_delete=models.CASCADE, default=None)
    judge_date = models.DateTimeField(blank=False, null=False, auto_now_add=True)
