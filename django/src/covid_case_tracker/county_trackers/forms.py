from django import forms
from .models import Tracker

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = [
            'title',
            'cases',
            'deaths',
            'prob_deaths'
        ]
