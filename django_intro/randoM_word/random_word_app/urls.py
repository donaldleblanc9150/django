from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("make_word", views.generate_word),
    path("reset", views.reset),
]
