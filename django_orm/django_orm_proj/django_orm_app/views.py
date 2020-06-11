from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    context = {
        "all_users": User.objects.all(),
    }
    return render(request, "index.html", context)


def add_user(request):
    User.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        email=request.POST["email"],
        fav_number=request.POST["fav_number"],
        motto=request.POST["motto"],
    )
    return redirect("/")


def view_user(request, user_id):
    context = {
        "this_user": User.objects.get(id=user_id),
    }
    return render(request, "view.html", context)
