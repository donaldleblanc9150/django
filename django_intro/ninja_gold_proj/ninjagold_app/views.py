from django.shortcuts import render, redirect
import random


def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0
    if "my_string" not in request.session:
        request.session["my_string"] = []
    context = {
        "my_string": request.session["my_string"]
    }
    return render(request, "index.html", context)


def process_gold(request):
    score = request.session["gold"]
    if score > 0:
        request.session["my_string"] = f"WooHoo! You earned {score} "

    else:
        request.session[
            "my_string"] = f"Shucks! You lost - you will have to wash dishes to pay off your debt! {score} "

    if request.POST['location'] == "farm_gold":
        # If we went to the farm, let's generate our gold
        request.session['gold'] += random.randint(10, 20)

    if request.POST['location'] == "cave_gold":
        request.session['gold'] += random.randint(5, 10)

    if request.POST['location'] == "house_gold":
        request.session['gold'] += random.randint(2, 25)

    if request.POST['location'] == "casino_gold":
        request.session['gold'] += random.randint(-50, 50)

    print(score)
    print(request.POST["location"])
    return redirect('/')
