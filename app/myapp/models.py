from django.db import models
from django.contrib.auth.models import User


class Teachers(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

class Vendors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Wallet(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)

class Calendar(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_eating = models.DateField(auto_now=False, auto_now_add=True)
    eaten = models.BooleanField(default=0)
    cancelled = models.BooleanField(default=0)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    food = models.CharField(max_length=250)