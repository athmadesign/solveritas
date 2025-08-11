from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('product-detail', views.product_detail, name='product-detail'),
    path('blog', views.blog, name='blog'),
]
