from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Ticket', TicketView, basename='ticket')
router.register('Ticket-Message', TicketMessage, basename='messages ticket')



urlpatterns = [
    path("", include(router.urls))

    ]