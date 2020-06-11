from django.shortcuts import HttpResponse, redirect, render

# def index(request):
#     # return HttpResponse("<h1>Hello this is working</h1>")
#     context = {
#         "first_name": "Donald",
#         "users": [
#             "Mike Myers",
#             "Carey Siles",
#             "Portia Mason"
#         ]
#     }
#     return render(request, "index.html", context)

def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)
    # return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request):
    return HttpResponse("placeholder to display blog number: {number}")

def edit(request):
    return HttpResponse("placeholder to edit blog {number}")

def destroy(request):
    return redirect("/")