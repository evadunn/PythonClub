import club
from club.views import MeetingDetail
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event, Meetingminutes, Meeting, Resource
import datetime
from django.urls import reverse_lazy, reverse

# Create your tests here.
class EventTest(TestCase): 
    def setUp(self): 
        self.type=Event(eventtitle='History Dept conference')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'History Dept conference')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Weekly meeting')
        self.user=User(username='user1')
        self.meeting=Meeting(meetingtitle='Weekly meeting', meetingdate=datetime.date(2021, 10, 10), meetingtime=datetime.time(10, 30, 00), meetinglocation='Conference room 1', meetingagenda='New Hires')
        
    def test_string(self):
        self.assertEqual(str(self.type), 'Weekly meeting')

    def test_meeting(self):
        self.percent = self.meeting
        self.assertEqual(str(Meeting._meta.db_table),'Meeting')

class NEW_ResourceTest_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='p@ssw0rd1')
        self.type=Resource.objects.create(resourcename='resourcename')
        self.resource=Resource.objects.create(resourcename='Weekly meeting', resourcetype='Admin', resourceURL='http://www.supplies.com', dateentered=datetime.date(2021, 10, 10), resourcedescription='Supplies')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newResource.html'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newResource/.html/')
