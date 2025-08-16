from django.shortcuts import render, get_object_or_404
from . models import BlogPost

# Create your views here.
def blog(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    return render(request, 'core/blog.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    context = {'blog':blog}
    return render(request, 'core/blog_detail.html', context)