from typing import Dict
from rest_framework import serializers

from product.models import Product


def product_serializer(product: Product) -> Dict:
    data: Dict = {

        'name': product.name,
        'description': product.description,
        'image': product.image,
        'sku': product.sku,
        'price': product.price,
        'created_at': str(product.category.created_at),
        'updated_at': str(product.category.updated_at),
    }
    return data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
