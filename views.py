from django.shortcuts import render, get_object_or_404
from .models import Event, Meetingminutes, Meeting, Resource
from django.urls import reverse_lazy
from .forms import ResourceForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def getEvent(request):
    Event_list = Event.objects.all()
    return render(request, 'club/Event.html', {'Event_list': Event_list})

def MeetingDetail(request, id):
    event=get_object_or_404(Event, pk=id)
    return render(request, 'club/MeetingDetail.html', {'event' : event})

def Resource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/resource.html', {'form': form})