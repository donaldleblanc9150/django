from django.shortcuts import render, redirect, HttpResponse


def index(request):
    # this is the route that shows the form
    return render(request, "index.html")
    # return HttpResponse("you have reached the page")


def create_user(request):
    # this is the route that processes the form
    print("Got Post Info............")
    name_from_form = request.POST["name"]
    email_from_form = request.POST["email"]
    request.session["name"] = request.POST["name"]
    request.session["counter"] = 100
    context = {
        "name_on_template": name_from_form,
        "email_on_template": email_from_form
    }
    # print(name_from_form)
    # print(email_from_form)
    # return render(request, "show.html", context)
    return redirect("/success")


def success(request):
    # this is the success route
    return render(request, "success.html")
