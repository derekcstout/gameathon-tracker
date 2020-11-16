from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, FormView, ListView, TemplateView
from django.urls import reverse_lazy
from .models import Gameboard
from .forms import GameboardForm, SearchGameboard
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return HttpResponse("Hello there, this is the beginning of the gameathon-tracker.")


@login_required
def gameboard(request):
    return render(request, "gameboard/gameboard.html")


def standings(request):
    return render(request, "standings/standings.html")


class NewGameboard(CreateView):
    model = Gameboard
    form_class = GameboardForm
    template_name = 'gameboard/new_gameboard.html'
    success_url = reverse_lazy('gameboard')


class GameboardSearchResults(ListView):
    model = Gameboard
    template_name = 'gameboard/searchresults.html'

    def get_queryset(self):
        return Gameboard.objects.filter(gameboard_name__icontains='Game')


class GameboardSearch(TemplateView):
    template_name = 'gameboard/search.html'

