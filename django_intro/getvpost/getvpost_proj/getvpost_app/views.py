from django.shortcuts import HttpResponse, render, redirect

# def index(request):
#     # return HttpResponse("this is the page you were looking for")
#     if request.method == "GET":
#         print("a GET request is being made to this route")
#         return render(request, "index.html")
#     if request.method == "POST":
#         print("a POST request is bieng made to this route")
#         return redirect("/")

def index(request):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        print(request.POST)
    return render(request, "index.html")

def new(request):
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
    return render(request, "index.html")