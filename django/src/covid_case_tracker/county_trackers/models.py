from django.db import models

# Create your models here.

class Tracker(models.Model):
    def __init__(self,title,cases,deaths, prob):
        self.title           = title
        self.cases           = cases
        self.deaths          = deaths
        self.prob_deaths     = prob
        
    title           = models.CharField(max_length=32)
    cases           = models.IntegerField()
    deaths          = models.IntegerField()
    prob_deaths     = models.IntegerField()