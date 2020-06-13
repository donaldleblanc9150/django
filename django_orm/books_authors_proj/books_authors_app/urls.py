from django.urls import path
from . import views

urlpatterns = [
    path("authors/<int:id>/delete", views.delete_author),
    path("book/<int:id>/delete", views.delete_book),
    path("authors/<int:id>", views.view_author),
    path("authors/new", views.add_author),
    path("authors/", views.authors),
    path("book/<int:id>/update", views.update_book),
    path("book/<int:id>/edit", views.edit_book),
    path("book/<int:id>", views.view_book),
    path("new", views.add_book),
    path("", views.index),
]
