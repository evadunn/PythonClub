from django.shortcuts import render, get_object_or_404
from .models import Event, Meetingminutes, Meeting, Resource
from django.urls import reverse_lazy
from .forms import newResourceForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def getEvent(request):
    Event_list = Event.objects.all()
    return render(request, 'club/Event.html', {'Event_list': Event_list})

def MeetingDetail(request, id):
    event=get_object_or_404(Event, pk=id)
    return render(request, 'club/MeetingDetail.html', {'event' : event})

@login_required
def newResource(request):
    form=newResourceForm

    if request.method=='POST':
        form=newResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=newResourceForm()
    else:
        form=newResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')
