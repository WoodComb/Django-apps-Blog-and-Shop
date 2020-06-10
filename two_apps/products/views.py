from django.shortcuts import render
from django.views.generic import ListView
from .models import Products
# Create your views here.
class ProductListView(ListView):
    model = Products
    template_name = 'products/products_home.html'
    context_object_name = 'products'
    ordering = ['updated_at']
