from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, FormView, ListView, TemplateView
from django.urls import reverse_lazy, reverse
from .models import Gameboard
from .forms import GameboardForm, SearchGameboard
from django.contrib.auth.decorators import login_required
from django.db.models import Q


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
        query = self.request.GET.get('q')
        object_list = Gameboard.objects.filter(
            Q(gameboard_name__icontains=query)
        )
        return object_list


class GameboardSearch(FormView):
    template_name = 'gameboard/search.html'
    form_class = SearchGameboard


def JoinGameboard(request):
    gameboard_join = get_object_or_404(Gameboard, id=request.POST.get('join_button'))
    gameboard_join.gameboard_players.add(request.user)
    return HttpResponseRedirect(reverse('search'))





