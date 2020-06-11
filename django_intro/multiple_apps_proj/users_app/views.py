from django.shortcuts import render, HttpResponse, redirect


def register(request):
    return HttpResponse("Placeholder for users to create a new record")


def login(request):
    return HttpResponse("Placeholder for users to log in")


def users(request):
    return HttpResponse("Placeholder to later display all the lists of users")
