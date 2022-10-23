from django.db import models

from product.models import Category


class User(models.Model):
    title = models.CharField(max_length=60)
    username = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    categories = models.ManyToManyField(Category, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)
    public_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
