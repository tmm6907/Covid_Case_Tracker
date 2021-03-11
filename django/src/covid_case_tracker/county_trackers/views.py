from django.shortcuts import render

from .models import Tracker

# Create your views here.
def county_detail_view(request):
    obj = Tracker.objects.get(id=7)
    context = {
        'object': obj
    }
    return render(request, 'county_trackers/detail.html', context)