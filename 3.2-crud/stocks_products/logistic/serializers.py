from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta():
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        [StockProduct.objects.create(stock=stock, **pos) for pos in positions]

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for pos in positions:
            StockProduct.objects.update_or_create(id=instance.id, defaults=pos)

        return stock
