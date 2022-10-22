from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'title', 'code']
    list_filter = ['code']
    search_fields = ['title']
    filter_horizontal = ['categories']

@admin.register(Category)
class CtegoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['id', 'name_product', 'parent',   'description', 'is_enable']
    list_filter = ['parent']
    search_fields = ['parent']
