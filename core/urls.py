from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('download', views.download, name='download'),
    path('case', views.case, name='case'),
    path('feedback', views.feedback, name='feedback'),
]
