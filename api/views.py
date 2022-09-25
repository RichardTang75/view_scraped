from django.shortcuts import render

from rest_framework import generics
from .models import ScrapedItem
from .serializers import ScrapedItemSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = ScrapedItem.objects.all()
    serializer_class = ScrapedItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScrapedItem.objects.all()
    serializer_class = ScrapedItemSerializer
