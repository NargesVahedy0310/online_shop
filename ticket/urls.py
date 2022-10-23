from django.urls import path
from .views import *

urlpatterns = [
    path('ticket/', UserView.as_view()),
    path('ticket/admin/', AdminListView.as_view()),
    path('ticket/admin/<int:pk>/', AdminDetaile.as_view())
]