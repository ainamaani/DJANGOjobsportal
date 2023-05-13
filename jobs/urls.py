from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addjob/',views.newjob, name='newjob'),
    path('jobs/',views.jobs,name='jobs'),
    path('jobs/<int:id>/',views.details,name='details')
    
]