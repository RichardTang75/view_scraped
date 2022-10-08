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

# class ScrapedItemFilter(filters.FilterSet):
#     link = filters.CharFilter(field_name='WantItem__link', lookup_expr='icontains', distinct=True, label='link')
#     class Meta:
#         model = ScrapedItem
#         fields = ['WantItem__link']

# class ScrapedItemFilter(filters.FilterSet):
#     class Meta:
#         model = ScrapedItem
#         fields = {
#             'title': ['icontains'],
#             'description': ['icontains'],
#             'link': ['icontains'],
#             'date': ['gte', 'lte'],
#             'last_seen': ['gte', 'lte'],
#             'WantItem__link': ['icontains'],
#         }