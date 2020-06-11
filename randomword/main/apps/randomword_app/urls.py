from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word/generate$', views.generate),
    url(r'^reset$', views.reset),
  ]