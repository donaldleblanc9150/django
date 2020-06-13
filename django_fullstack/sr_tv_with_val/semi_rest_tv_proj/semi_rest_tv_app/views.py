from django.shortcuts import render, HttpResponse, redirect
from .models import *


def index(request):
    # context = {
    #     "all_the_shows": Show.objects.all()
    # }
    return redirect("/shows")


def new_show(request):
    return render(request, "new_show.html")


def create_show(request):
    post = request.POST

    Show.objects.create(
        title=post["title"],
        network=post["network"],
        desc=post["desc"],
        release_date=post["release_date"]
    )

    return redirect("/")
    # return HttpResponse("You have reached the CREATE a Show route")


def view_show(request, id):
    view_one_show = Show.objects.get(id=id)
    context = {
        "view_one_show": view_one_show
    }

    return render(request, "view_show.html", context)
    # return HttpResponse("You have reached the VIEW a Specific Show Route")

def all_shows(request):
    context = {
        "all_the_shows": Show.objects.all()
    }
    return render(request, "index.html", context)


def edit_show(request, id):
    view_one_show = Show.objects.get(id=id)
    view_one_show.release_date = view_one_show.release_date.strftime("%Y-%m-%d")
    context = {
        "view_one_show": view_one_show
    }
    return render(request, "update_show.html", context)
    # return HttpResponse("You have reached the EDIT SHOW Route")


def update_show(request, id):
    show_to_update = Show.objects.get(id=id)

    show_to_update.title = request.POST["title"]
    show_to_update.network = request.POST["network"]
    show_to_update.desc = request.POST["desc"]
    show_to_update.release_date = request.POST["release_date"]
    
    show_to_update.save()

    return redirect("/")

def delete_show(request, id):
    show_to_delete = Show.objects.get(id=id)

    show_to_delete.delete()
    
    return redirect("/")
