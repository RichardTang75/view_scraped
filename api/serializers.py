from rest_framework import serializers
from .models import ScrapedItem, WantItem, IgnoreItem

class ScrapedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedItem
        fields = '__all__'

class WantItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['item_id'] = ScrapedItemSerializer(instance.item_id).data
        return data
    class Meta:
        model = WantItem
        fields = '__all__'

class IgnoreItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['item_id'] = ScrapedItemSerializer(instance.item_id).data
        return data
    class Meta:
        model = IgnoreItem
        fields = '__all__'