from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models import TextField
from django.utils import timezone


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    picture = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class HateFood(models.Model):
    Food = models.CharField(max_length=200)
    Hate = models.CharField(max_length=200)
