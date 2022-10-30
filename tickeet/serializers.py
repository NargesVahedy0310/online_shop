from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'status', 'department', 'products')

class TicketMessageSerializer(serializers.ModelSerializer):
    # ticket = TicketSerializer(many=True, read_only=True)
    class Meta:
        model = MessageTicket
        fields = ('id', 'title', 'body', 'file', 'ticket')
        depth = 1
