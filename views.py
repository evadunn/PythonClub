from django.shortcuts import render
from .models import Event, Meetingminutes, Meeting

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def Event(request):
    Event_list = Event.objects.all()
    return render(request, 'club/Event.html', {'Event_list': Event_list})
