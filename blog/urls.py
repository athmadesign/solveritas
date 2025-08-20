from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/category/<slug:slug>/', views.blogs_by_category, name='blogs_by_category')
]
