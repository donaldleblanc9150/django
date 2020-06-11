from django.urls import path
from . import views

urlpatterns = [
    path("users/<int:user_id>", views.view_user),
    path("add_user", views.add_user),
    path("", views.index),
]
