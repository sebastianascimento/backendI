from django.urls import path
from products.models import Product
from products.views import ListAllProducts


urlpatterns=[
    path("",ListAllProducts.as_view()),
    path("<slug>" , ProductDetailView())
]