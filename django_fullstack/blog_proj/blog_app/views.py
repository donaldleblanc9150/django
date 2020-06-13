from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *

def update(request, id):
    errors = Player.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/player/edit" + id)
    else:
        player = Player.objects.get(id=id)
        player.first_name = request.POST["first_name"]
        player.last_name = request.POST["last_name"]
        player.team = request.POST["team"]
        player.save()
        messages.success(request, "Player successfully updated")
        
        return redirect("/")

def index(request):
    context = {
        "all_players" : Player.objects.all()
    }
    return render(request, "index.html", context)

def add_player(request):
    errors = Player.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        player = Player.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        team=request.POST["team"]
    )
        
    return redirect("/")