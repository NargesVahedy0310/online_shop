from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework import generics
class TicketView(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options']
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer
    def get_queryset(self):
        if self.request.user.is_staff:
            return Ticket.objects.all()
        return Ticket.objects.filter(user_id=self.request.user.id)

class TicketMessage(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketMessageSerializer
    http_method_names = ['get', 'post', 'head', 'options']

    def get_queryset(self):
        if self.request.user.is_staff:
            return MessageTicket.objects.all()
        return MessageTicket.objects.filter(users_id=self.request.user.id)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    # def perform_create(self, serializer):
    #     serializer.save()
