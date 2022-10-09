from django.shortcuts import render

from rest_framework import generics, permissions
from .models import ScrapedItem, WantItem, IgnoreItem
from .serializers import ScrapedItemSerializer, WantItemSerializer, IgnoreItemSerializer

from django_filters import rest_framework as filters
from api.filters import ScrapedItemFilter

class ItemList(generics.ListCreateAPIView):
    queryset = ScrapedItem.objects.filter(wantitem__isnull=True).filter(ignoreitem__isnull=True).order_by('-date')
    serializer_class = ScrapedItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScrapedItemFilter
    # items should be read only
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScrapedItem.objects.all()
    serializer_class = ScrapedItemSerializer
    # items should be read only
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WantItemList(generics.ListCreateAPIView):
    queryset = WantItem.objects.all()
    serializer_class = WantItemSerializer

class IgnoreItemList(generics.ListCreateAPIView):
    queryset = IgnoreItem.objects.all()
    serializer_class = IgnoreItemSerializer