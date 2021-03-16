from django.db import models

# Create Manager for Tracker model
#class TrackerManager(models.Manager):
   # def create_tracker(self, title, cases, deaths, prob):
       # tracker = self.create(titletitle, cases, deaths, prob)
       # return tracker

# Tracker Model for database
class Tracker(models.Model):    
    title           = models.CharField(max_length=32)
    cases           = models.CharField(max_length=9)
    deaths          = models.CharField(max_length=9)
    prob_deaths     = models.IntegerField()

    #objects         = TrackerManager()
    