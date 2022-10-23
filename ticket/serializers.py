from rest_framework import serializers

from .models import *
from product.serializers import CategorySerializer

class UserSerializer(serializers.ModelSerializer):
    categories = CategorySerializer

    class Meta:
        model = User
        fields = ['id', 'title', 'username', 'description',  'email', 'created_time', 'categories']

class AdminSerializers(serializers.ModelSerializer):
    users = UserSerializer
    class Meta:
        fields = ['id', 'users']

