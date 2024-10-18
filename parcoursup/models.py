from django.db import models
from django.contrib.auth.models import User


class Establishment(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    formations = models.ManyToManyField('Formation', through='hasFormation')

class Formation(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    applications = models.ManyToManyField(User, through='Application')

class Application(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

class hasFormation(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)