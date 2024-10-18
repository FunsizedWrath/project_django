from django.db import models
from django.contrib.auth.models import User


class Establishments(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    formation = models.ManyToManyField('Formations', through='Offers')

class Formations(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    application = models.ManyToManyField(User, through='Applications')

class Applications(models.Model):
    formation = models.ForeignKey(Formations, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

class Offers(models.Model):
    establishment = models.ForeignKey(Establishments, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formations, on_delete=models.CASCADE)