from django.urls import path
from . import views

urlpatterns = [
    path("author/new", views.add_author),
    path("books/<int:id>", views.view_book),
    path("new", views.add_book),
    path("", views.index),
]
