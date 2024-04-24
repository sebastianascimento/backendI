from django.shortcuts import render

# Create your views here.
from products.models import Product
# Create your views here.

class ListAllProducts(ListView):
    model=Product
    queryset=Product.objects.filter(enabled=True).all()


