from django.db import models

# Create your models here.

class Tracker(models.Model):
    title           = models.CharField(max_length=32)
    cases           = models.IntegerField()
    deaths          = models.IntegerField()
    prob_deaths     = models.IntegerField()