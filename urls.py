from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'), 
   path('getEvent/', views.getEvent, name='Event'), 
   path('MeetingDetail/<int:id>', views.MeetingDetail, name='Detail'),
   path('Resource/', views.Resource, name='Resource'),
]
