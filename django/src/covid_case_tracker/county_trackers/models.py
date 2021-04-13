from django.db import models

# Tracker Model for database
class Tracker(models.Model):    
    title           = models.CharField(max_length=32)
    cases           = models.CharField(max_length=9)
    deaths          = models.CharField(max_length=9)
    prob_deaths     = models.IntegerField()
    time_log        = models.DateTimeField(auto_now_add = True)
    