from django.shortcuts import render

from .tasks import main

import time
# Create your views here.

def background_view():
    index = 1
    while True:
        main.covidpg(index)
        index+=1

        time_wait = 60
        time.sleep(time_wait*1440)