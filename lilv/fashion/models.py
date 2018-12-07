from django.db import models

# Create your models here.
class User(models.Model):
    tel = models.ImageField()
    password = models.CharField(max_length=(100))


# 轮播模型
class Lunbo(models.Model):
    img = models.CharField(max_length=100)
    wen = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)

    class Meta:
        db_table = 'Lunbo'