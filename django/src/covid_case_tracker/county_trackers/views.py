from django.shortcuts import render
from .forms import TrackerForm
from .models import Tracker

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