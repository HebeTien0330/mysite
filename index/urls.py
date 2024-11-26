from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("media/", views.blog, name="media"),
    path("games/", views.games, name="games"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
]
