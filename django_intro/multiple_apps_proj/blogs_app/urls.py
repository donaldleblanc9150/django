from django.urls import path
from . import views

urlpatterns = [
    path("<number>/delete", views.destroy),
    path("<number>/edit", views.edit),
    path("<int:number>", views.show),
    path("create", views.create),
    path("new", views.new),
    path("", views.index),
]
