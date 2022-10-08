from rest_framework import serializers
from .models import ScrapedItem, WantItem, IgnoreItem

class ScrapedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedItem
        fields = '__all__'

class WantItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantItem
        fields = '__all__'

class IgnoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IgnoreItem
        fields = '__all__'