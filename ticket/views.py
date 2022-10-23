from django.shortcuts import render

from rest_framework import filters
from rest_framework import generics, mixins, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

class UserView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdminListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminDetaile(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer