from django.urls import path
from . import views
from django.http import Http404



urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('case', views.case, name='case'),
    path('feedback', views.feedback, name='feedback'),
]
