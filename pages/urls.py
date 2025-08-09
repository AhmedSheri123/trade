from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SubmittedComplaints', views.SubmittedComplaints, name='SubmittedComplaints'),
    path('SubmitInfo', views.SubmitInfo, name='SubmitInfo'),
    path('SubmitComplaint', views.SubmitComplaint, name='SubmitComplaint')
]
