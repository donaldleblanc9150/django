from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    if 'counter' not in request.session:
        request.session["counter"] = 0
        request.session['random'] = get_random_string(
            length=14, allowed_chars="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")

    context = {
        "counter": request.session["counter"]
    }
    return render(request, "index.html", context)

    # return HttpResponse("You have reached the RandomWord Generator Page --- This link works!!")


def generate_word(request):

    request.session["random"] = get_random_string(
        length=14, allowed_chars="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
    if request.GET.get("generate") == "generate":
        request.session["counter"] += 1

    print(request.GET)
    return redirect("/")
    # return HttpResponse("You have reached the reset page!")


def reset(request):
    if request.GET.get("reset") == "reset":
        request.session["counter"] = 0
        request.session["random"] = ""
    return redirect('/')
