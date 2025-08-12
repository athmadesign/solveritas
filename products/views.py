from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def products(request):
    products = Product.objects.all()
    return render(request, 'core/products.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'core/product_detail.html', {'product': product})

def products_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'core/products.html', {'category': category, 'products': products})
