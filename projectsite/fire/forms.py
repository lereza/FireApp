from django import forms
from .models import FireStation, Incident, Locations, FireTruck,Firefighters

class FireStationForm(forms.ModelForm):
    class Meta:
        model = FireStation
        fields = ['name', 'latitude', 'longitude', 'address', 'city', 'country']

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['location', 'date_time', 'severity_level', 'description']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ['name', 'latitude', 'longitude', 'address', 'city', 'country']


class FireTruckForm(forms.ModelForm):
    class Meta:
        model = FireTruck
        fields = ['truck_number', 'model', 'capacity', 'station']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['station'].queryset = FireStation.objects.all()  # Provide queryset for the station field

class FirefightersForm(forms.ModelForm):
    class Meta:
        model = Firefighters
        fields = ['name', 'rank', 'experience_level', 'station']

