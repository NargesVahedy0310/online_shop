from django.shortcuts import render

from rest_framework import filters
from rest_framework import generics, mixins, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

class ProductListView(generics.ListCreateAPIView):
    filterset_fields = ['categories']
    filter_backends = [DjangoFilterBackend]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetaile(generics.RetrieveAPIView):
    queryset = Category
    serializer_class = CategorySerializer

