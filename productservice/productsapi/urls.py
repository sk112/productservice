from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('products-list/', ListProducts.as_view(), name='product-list'),
    path('product-details/<str:pk>/', ProductDetails.as_view(), name='product-details'),
    path('search/', ProductSearch.as_view(), name='search'),
]