from django.shortcuts import render, get_object_or_404
from . models import BlogPost, BlogCategory
from django.db.models import Q


# Create your views here.
def blog(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    return render(request, 'core/blog.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    context = {'blog':blog}
    return render(request, 'core/blog_detail.html', context)

def blogs_by_category(request, slug):
    category = get_object_or_404(BlogCategory, slug=slug)

    # Include products of the category + all its subcategories
    blogs = BlogPost.objects.filter(
        category__slug=slug
    )

    return render(request, 'core/blog.html', {
        'category': category,
        'blogs': blogs
    })
