from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return HttpResponse("You have reached the Hogwarts INdex page")
