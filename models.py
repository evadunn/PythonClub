from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255, null=True, blank=True)
    meetingagenda=models.TextField()

    def percentfilled(self):
        self.percentfilled=self.meetinglocation
        return self.meetinglocation

    def totalattendees(self):
        self.totalattendees=self.meetinglocation -self.percentfilled

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='Meeting'

class Meetingminutes(models.Model):
    meetingminutesid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    def __str__(self):
        return self.meetingminutes

    class Meta:
        db_table='Meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceURL=models.URLField()
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='Resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField()
    eventtime=models.CharField(max_length=255)
    eventdescription=models.TextField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
       
    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='Event'

    