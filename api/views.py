from django.shortcuts import render

from rest_framework import generics, permissions, mixins
from .models import ScrapedItem, WantItem, IgnoreItem
from .serializers import ScrapedItemSerializer, WantItemSerializer, IgnoreItemSerializer

from django_filters import rest_framework as filters
from api.filters import ScrapedItemFilter

class ItemList(generics.ListAPIView):
    queryset = ScrapedItem.objects.filter(wantitem__isnull=True).filter(ignoreitem__isnull=True).order_by('-date')
    serializer_class = ScrapedItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScrapedItemFilter

class ItemDetail(generics.RetrieveAPIView):
    queryset = ScrapedItem.objects.all()
    serializer_class = ScrapedItemSerializer

class WantItemList(generics.ListCreateAPIView):
    queryset = WantItem.objects.all()
    serializer_class = WantItemSerializer

class IgnoreItemList(generics.ListCreateAPIView):
    queryset = IgnoreItem.objects.all()
    serializer_class = IgnoreItemSerializer

class WantItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WantItem.objects.all()
    # queryset = WantItem.objects.all().prefetch_related('item_id')
    serializer_class = WantItemSerializer

class IgnoreItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IgnoreItem.objects.all()
    serializer_class = IgnoreItemSerializer

class InteractWantItemList(generics.ListAPIView):
    queryset = WantItem.objects.filter(completed=False).order_by('view_order', '-judge_date')
    serializer_class = WantItemSerializer