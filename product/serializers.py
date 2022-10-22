from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_product', 'parent',   'description', 'is_enable']


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer
    class Meta:
        model = Product
        fields = ['id', 'title', 'code', 'price', 'price_after_discount', 'is_enable', 'categories']