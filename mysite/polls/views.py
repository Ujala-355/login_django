from django.shortcuts import render, HttpResponse,redirect
# from polls.views import *

def index(request):
    return HttpResponse("Welcome,to Django home page")


def login(request):
    return render(request, 'login.html')

