from django.shortcuts import render
from . models import Slider, Testimonial
from blog.models import BlogPost
from products.models import Product

# Create your views here.

def home(request):
    sliders = Slider.objects.filter(is_active=True).order_by('order')
    latest_blogs = BlogPost.objects.order_by('created_at')[:3]
    featured_products = Product.objects.filter(is_active=True)[:8]  # Show 8 products
    testimonials = Testimonial.objects.all()
    context = { 'sliders' : sliders, 'latest_blogs':latest_blogs, 'featured_products': featured_products, 'testimonials':testimonials}
    return render(request, 'core/index.html', context)

def about(request):
    testimonials = Testimonial.objects.all()
    context = {'testimonials':testimonials}
    return render(request, 'core/about.html', context)

def contact(request):
    return render(request, 'core/contact.html')


def case(request):
    return render(request, 'core/case.html')

def feedback(request):
    return render(request, 'core/feedback.html')

def custom_404_view(request, exception):
    return render(request, 'core/404.html', status=404)