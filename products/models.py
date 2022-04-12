from django.db import models
from django.forms import CharField


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=2048, default='')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    calories = models.IntegerField(default=0)
    eda_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name
