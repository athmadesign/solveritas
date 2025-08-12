from .models import Category

def menu_categories(request):
    categories = Category.objects.filter(parent__isnull=True).prefetch_related('subcategories')
    return {'menu_categories': categories}
