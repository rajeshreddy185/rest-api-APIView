from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.Serializer):
    class Meta:
        models = Product
        fields = ('title', 'description')

    def create(self, validated_data):
        return Product.objects.create(**validated_data)