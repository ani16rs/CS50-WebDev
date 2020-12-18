from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def anmol(request):
    return HttpResponse("Hello, Anmol")

def anu(request):
    return HttpResponse("Hello, Anu")
