from django.shortcuts import render

from .tasks import main, display
from django.shortcuts import render
from county_trackers.models import Tracker
from background_task import background

import time
# Create your views here.

def background_view(request):
    while True:
        main.covidpg()
        display.county_detail_view(request)
        time_wait = 60
        time.sleep(time_wait*1440)