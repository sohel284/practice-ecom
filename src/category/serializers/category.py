from typing import Dict

from rest_framework import serializers

from category.models import Category


def category_serializer(category: Category) -> Dict:
    data: Dict = {
        'id': category.id,
        'name': category.name,
        'type': category.type,
        'image': category.image,
        'created_at': str(category.created_at),
        'updated_at': str(category.updated_at),
    }
    return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        exclude = ('created_at', 'updated_at')
