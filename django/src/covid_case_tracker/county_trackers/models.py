from django.db import models

# Create your models here.
class TrackerManager(models.Manager):
    def create_tracker(self, title, cases, deaths, prob):
        tracker = self.create(title = title, cases = cases, deaths = deaths, prob_deaths = prob)
        # do something with the book
        return tracker

class Tracker(models.Model):    
    title           = models.CharField(max_length=32)
    cases           = models.IntegerField()
    deaths          = models.IntegerField()
    prob_deaths     = models.IntegerField()

    objects         = TrackerManager()
    