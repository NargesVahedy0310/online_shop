from django.db import models
from product.models import *
from django.contrib.auth.models import User
class Ticket(models.Model):
    STATUS = [
        ('open', 'باز'),
        ('close', 'بسته'),

    ]
    DEPARTMENT =[
        ('teacher', 'معلم'),
        ('money', 'مالی'),
    ]
    MOBILE = 'mobile'
    LAPTOP = 'laptap'
    PRODUCTS = [
        (MOBILE, 'مبایل'),
        (LAPTOP, 'لپ تاپ'),
    ]
    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=10)
    department = models.CharField(choices=DEPARTMENT, default=DEPARTMENT[0], max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    products = models.CharField(choices=PRODUCTS, default=PRODUCTS[0], max_length=10)
    def __str__(self):
        return self.status


class MessageTicket(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)
    file = models.FileField(blank=True, upload_to='File')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return self.title

