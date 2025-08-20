from django.urls import path
from . import views
from django.http import Http404

handler404 = 'core.views.custom_404_view'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('download', views.download, name='download'),
    path('case', views.case, name='case'),
    path('feedback', views.feedback, name='feedback'),
]
