from django.db import models

# Create your models here.


class Producr(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    condity=models.IntegerField()
    objects = models.Manager() 