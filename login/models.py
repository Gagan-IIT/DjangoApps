from django.db import models
from django import forms

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length = 120)
    password = models.CharField(max_length = 32)