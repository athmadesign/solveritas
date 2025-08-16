from .models import Category
from blog.models import BlogCategory

def menu_categories(request):
    categories = Category.objects.filter(parent__isnull=True).prefetch_related('subcategories')
    return {'menu_categories': categories}

def blog_categories(request):
    blog_categories = BlogCategory.objects.all()
    return {'blog_categories':blog_categories}