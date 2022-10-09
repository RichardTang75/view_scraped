from django_filters import rest_framework as filters

from .models import ScrapedItem, WantItem, IgnoreItem

class ScrapedItemFilter(filters.FilterSet):
    class Meta:
        model = ScrapedItem
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
            'link': ['icontains'],
            'date': ['gte', 'lte'],
            'last_seen': ['gte', 'lte'],
        }