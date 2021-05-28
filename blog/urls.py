from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="BlogHome"),
    path("blogposts/<int:id>", views.blogposts, name="BlogPosts")
]
