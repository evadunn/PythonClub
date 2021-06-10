from django import forms
from .models import Event, Meetingminutes, Meeting, Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'
        