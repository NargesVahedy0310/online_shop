from django.urls import path
from .views import *
urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetaile.as_view()),

]