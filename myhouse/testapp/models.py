from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)




class Entity(models.Model):
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    properties = models.ManyToManyField(Property)
