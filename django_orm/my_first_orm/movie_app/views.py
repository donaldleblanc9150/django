from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    context = {
        "all_the_movies": Movie.objects.all()
    }
    # return HttpResponse("You have reached the MovieApp INDEX page")
    return render(request, "index.html", context)
