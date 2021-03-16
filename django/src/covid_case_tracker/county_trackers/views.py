from django.shortcuts import render
from django.http import HttpResponse
from .forms import TrackerForm
from .models import Tracker
from .tasks import covidpg

# Create your views here.
def tracker_create_view(request):
    form = TrackerForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = TrackerForm()

    context = {
        'form': form
    }
    return render(request, 'county_trackers/county_create.html', context)

def county_detail_view(request):
    objs = Tracker.objects.all
    context = {
        'objects': objs
    }  
    return render(request, 'county_trackers/county_detail.html', context)

def background_view(request):
    time_wait = 60*1440
    covidpg(repeat = time_wait, repeat_until = None)
    return HttpResponse('<h2>Successful Process</h2>')

