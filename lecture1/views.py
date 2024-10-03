from django.http import HttpResponse
from django.shortcuts import render

def fx(request):
    return HttpResponse("<h1>Radhe Radhe</h1>")

def fx2(request):
    return HttpResponse("Bharat mata ki jai")