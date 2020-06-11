from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    context = {
        "all_dojos": Dojos.objects.all(),
    }
    return render(request, "index.html", context)
    # return HttpResponse("You have reached the link for the Dojo Ninja App")


def add_dojo(request):
    Dojos.objects.create(
        dojo_name=request.POST["dojo_name"],
        city=request.POST["city"],
        state=request.POST["state"],
        desc=request.POST["desc"],
    )
    return redirect("/")


def add_ninja(request):
    Ninjas.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        dojo=Dojos.objects.get(id=request.POST["dojo"]),
    )
    return redirect("/")


def delete_dojo(request, dojo_id):
    dojo_to_delete = Dojos.objects.get(id=dojo_id)
    dojo_to_delete()
    return redirect("/")
