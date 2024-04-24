from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from posts.models import Post

class ListAllPost(ListView):
    model=Post
    queryset=Post.objects.filter(enabled=True).all()

class PostDetailView():

