from django.shortcuts import render
from django.http import HttpResponse
from .models import Tracker
from .tasks import covidpg

# Create your views here.
def county_detail_view(request):
    qs = Tracker.objects.all
    context = {
        'objects': qs
    }  
    return render(request, 'county_trackers/county_detail.html', context)

def background_view(request):
    time_wait = 60*1440
    covidpg(repeat = time_wait, repeat_until = None)
    return HttpResponse('<h2>Successful Process</h2>')

