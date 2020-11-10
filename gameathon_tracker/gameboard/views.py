from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello there, this is the beginning of the gameathon-tracker.")


def gameboard(request):
    return render(request, "gameboard/gameboard.html")


def standings(request):
    return HttpResponse("<h1>This is the standings page!!!</h1>")

