
from county_trackers.models import Tracker
from background_task import background
from django.shortcuts import render

@background
def county_detail_view(request):
    objs = Tracker.objects.all
    context = {
        'objects': objs
    }  
    return render(request, 'county_trackers/county_detail.html', context)