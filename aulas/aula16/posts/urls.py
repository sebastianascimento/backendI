
from django.urls import path

from posts.views import ListAllPost

    urlpatterns = [
        path("", ListAllPost.as_post()) 
    ]