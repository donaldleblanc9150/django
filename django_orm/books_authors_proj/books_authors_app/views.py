from django.shortcuts import render, redirect, HttpResponse
from .models import Author, Books


def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Books.objects.all()
    }
    return render(request, "index.html", context)


def add_book(request):
    my_book = Books.objects.create(
        title=request.POST["title"],
        desc=request.POST["desc"],
    )
    return redirect("/")


def add_author(request):
    return HttpResponse("You have reached the ADD Author page")


def view_book(request, id):
    view_one_book = Books.objects.get(id=id)
    context = {
        "view_one_book": view_one_book,
    }
    return render(request, "view_book.html", context)
