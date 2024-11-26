from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("media/", views.media, name="media"),
    path("about/", views.about, name="about"),
]
