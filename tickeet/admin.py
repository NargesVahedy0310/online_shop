from django.contrib import admin
from .models import *

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ['id', 'status', 'department']
@admin.register(MessageTicket)
class MessagesTicketAdmin(admin.ModelAdmin):
    model = MessageTicket
    list_display = ['id', 'title', 'body']
