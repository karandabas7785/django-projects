#from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
  #return HttpResponse("hello World")
  return render(request,"home.html")
def about(request):
  #return HttpResponse("MY about respeinse")
  return render(request,"about.html")