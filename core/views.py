from django.shortcuts import render
from . models import Slider

# Create your views here.

def home(request):
    sliders = Slider.objects.filter(is_active=True).order_by('order')
    context = { 'sliders' : sliders}
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')



def blog(request):
    return render(request, 'core/blog.html')

def download(request):
    return render(request, 'core/download.html')

def case(request):
    return render(request, 'core/case.html')

def feedback(request):
    return render(request, 'core/feedback.html')