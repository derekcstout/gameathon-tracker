from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, FormView, ListView
from django.urls import reverse_lazy, reverse
from .models import Gameboard, PlayerGameboard
from .forms import GameboardForm, SearchGameboard
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum


@login_required(login_url="/players/login")
def gameboard(request):
    gameboards = Gameboard.objects.filter(gameboard_players=request.user)
    totals = PlayerGameboard.objects.annotate(points_sum=Sum('player_gameboard__points_awarded')).filter(
        gameboard_id__in=gameboards)

    context = {
        'totals': totals,
        'gameboards': gameboards
    }
    return render(request, "gameboard/gameboard.html", context)


def load_pieces(request):
    gameboard = request.GET.get('gameboard_id')
    totals = PlayerGameboard.objects.annotate(points_sum=Sum('player_gameboard__points_awarded')).filter(
        gameboard_id=gameboard)
    return render(request, "gameboard/load_pieces.html", {'totals': totals})


def load_scores(request):
    gameboard = request.GET.get('gameboard_id')
    totals = PlayerGameboard.objects.annotate(points_sum=Sum('player_gameboard__points_awarded')).filter(
        gameboard_id=gameboard)
    return render(request, "standings/load_scores.html", {'totals': totals})


@login_required(login_url="/players/login")
def standings(request):
    gameboards = Gameboard.objects.filter(gameboard_players=request.user)
    totals = PlayerGameboard.objects.annotate(points_sum=Sum('player_gameboard__points_awarded')).filter(
        gameboard_id__in=gameboards)

    context = {
        'totals': totals,
        'gameboards': gameboards
    }
    return render(request, "standings/standings.html", context)



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
