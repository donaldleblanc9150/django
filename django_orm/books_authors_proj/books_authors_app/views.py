from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Book.objects.all()
    }
    return render(request, "index.html", context)


def add_book(request):
    post = request.POST

    Book.objects.create(
        title=post["title"],
        desc=post["desc"],
        # books=Book.objects.get(id=post["authors"])
    )
    return redirect("/")


def authors(request):
    context = {
        "authors": Author.objects.all()
    }

    return render(request, "authors.html", context)


def add_author(request):
    one_author = Author.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        notes=request.POST["notes"],

    )
    return redirect("/authors")


def view_author(request, id):
    view_one_author = Author.objects.get(id=id)
    context = {
        "view_one_author": view_one_author,
        "all_books": Book.objects.all()
    }

    return render(request, "view_author.html", context)
    # return HttpResponse("you have reached the View Author page")


def view_book(request, id):
    view_one_book = Book.objects.get(id=id)
    context = {
        "view_one_book": view_one_book,
        "all_authors": Author.objects.all()
    }
    return render(request, "view_book.html", context)


def edit_book(request, id):
    view_one_book = Book.objects.get(id=id)
    context = {
        "view_one_book": view_one_book,
        "all_authors": Author.objects.all()
    }
    return render(request, "view_book.html", context)


def update_book(request, id):
    book_to_update = Book.objects.get(id=id)
    book_to_update.authors.add(Author.objects.get(id=request.POST["author_id"]))

    return redirect(request.META.get('HTTP_REFERER'))

def delete_book(request, id):
    book_to_delete = Book.objects.get(id=id)
    book_to_delete.delete()

    return redirect("/")


def delete_author(request, id):
    author_to_delete = Author.objects.get(id=id)
    author_to_delete.delete()

    return redirect(f"/authors")
