from django.db import models

# Create your models here.
class Works(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=1000, primary_key=True)

class Details(models.Model):
    username = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    phonenum = models.CharField(max_length=100)