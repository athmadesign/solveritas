from django.shortcuts import render
from . models import Slider
from blog.models import BlogPost

# Create your views here.

def home(request):
    sliders = Slider.objects.filter(is_active=True).order_by('order')
    latest_blogs = BlogPost.objects.order_by('created_at')[:3]
    context = { 'sliders' : sliders, 'latest_blogs':latest_blogs}
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def download(request):
    return render(request, 'core/download.html')

def case(request):
    return render(request, 'core/case.html')

def feedback(request):
    return render(request, 'core/feedback.html')

def custom_404_view(request, exception):
    return render(request, 'core/404.html', status=404)