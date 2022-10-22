from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    code = models.SmallIntegerField(null=True)
    price = models.BigIntegerField(blank=True, null=True)
    price_after_discount = models.BigIntegerField(blank=True, null=True)
    is_enable = models.BooleanField(default=True)
    caategores = models.ManyToManyField('Category', blank=True)
    created_time = models.DateTimeField(auto_now=True)
    public_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    parent = models.ForeignKey('self', null=True,on_delete=models.CASCADE)
    name_product = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now=True)
    public_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_product
