from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product
# Create your views here.

class ListAllProducts(ListView):
    model=Product
    queryset=Product.objects.filter(enabled=True).all()


class ProductDetailView()