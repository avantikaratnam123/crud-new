from django.db import models


class Register(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
