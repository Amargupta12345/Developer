from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello  You Must be loging in my file")


