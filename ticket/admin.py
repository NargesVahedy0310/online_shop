from django.contrib import admin

from .models import *

@admin.register(User)
class UserAdmin (admin.ModelAdmin):
    model = User
    list_display = ['id', 'title', 'username', 'email']
    list_filter = ['title']
    filter_horizontal = ['categories']
