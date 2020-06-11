from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

  # the index function is called when root is visited
def index(request):
  if "count" not in request.session:
    request.session["count"]=1
    request.session['random']=get_random_string(length=14)

  return render(request,'randomword_app/index.html')

def reset(request):
  request.session.clear()
  return redirect ('/')

def generate(request):
  request.session["count"]+=1
  request.session['random']=get_random_string(length=14)
  return redirect('/')
# Create your views here.
