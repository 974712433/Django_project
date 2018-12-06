from django.db import models

# Create your models here.
class User(models.Model):
    tel = models.ImageField()
    password = models.CharField(max_length=(100))