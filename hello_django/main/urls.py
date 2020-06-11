from django.urls import path

from . import views

urlpatterns = [
    # app-level routing
    # path function is like "glue"
    # when someone hits this route, call this function Django
    path("bunk/<int:my_num>", views.bunk_func),
    path("", views.index_func)
]