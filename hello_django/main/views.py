from django.shortcuts import render, HttpResponse

# Create your views here.
def index_func(request):
    # return HttpResponse("<h1>Hello from Django<h1>")
    context = {
        "first_name": "Morley",
        "users": [
            "Jason Brady",
            "Raymond Smith",
            "Yuri Chalmers"
        ],
        # "emails": [

        # ]
    }

    template_name = "index.html"

    return render(request, template_name, context)

def bunk_func(request, my_num):
    context = {
        "number": my_num
    }

    return render(request, "bunk.html", context)

# bunk_func(request, my_num=10)