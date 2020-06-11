from django.urls import path
from . import views

urlpatterns = [
    path("delete", views.delete_dojo),
    path("new_ninja", views.add_ninja),
    path("new_dojo", views.add_dojo),
    path("", views.index),
]
