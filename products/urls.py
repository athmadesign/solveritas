from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('product/<slug:slug>/', views.product_detail, name='product-detail'),
    path('products/<slug:slug>/', views.products_by_category, name='products_by_category'),
]
