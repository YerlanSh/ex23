from django.urls import path

from .views import *

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/new/', product_create, name='product_create'),
    path('products/<int:pk>/edit/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('categories/new/', category_create, name='category_create'),
    path('categories/<int:pk>/edit/', update_category, name='update_category'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),
]