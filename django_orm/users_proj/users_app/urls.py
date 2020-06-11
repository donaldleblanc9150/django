from django.urls import path
from . import views

urlpatterns = [
    path("new", views.create_user),
    path("", views.index),
]
