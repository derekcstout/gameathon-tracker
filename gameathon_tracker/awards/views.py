from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import formset_factory
from .models import Award
from .forms import AwardPointsForm, TestAwardForm
from gameboard.models import PlayerGameboard, Gameboard
from django.contrib.auth.models import User


def test(request):
    form_class = TestAwardForm
    if request.POST:
        form = form_class(request.user, request.POST)
        if request.method == 'POST':
            if form.is_valid():
                obj = Award()
                obj.player_gameboard_id = PlayerGameboard.objects.get(player_id=form.cleaned_data['player'], gameboard_id=form.cleaned_data['gameboard'])
                obj.position = form.cleaned_data['position']
                obj.points_awarded = form.cleaned_data['points_awarded']
                obj.team_game = form.cleaned_data['team_game']
                obj.game_name = form.cleaned_data['game_name']
                obj.save()
                return HttpResponseRedirect(reverse('gameboard'))
    else:
        form = form_class(request.user)

    return render(request, "awards/test.html", {'form': form})


def load_players(request):
    gameboard_id = request.GET.get('gameboard_id')
    players = User.objects.filter(playergameboard__gameboard_id=gameboard_id)
    return render(request, "awards/load_players.html", {'players': players})


class AddPointsView(CreateView):
    model = Award
    template_name = 'awards/awardpoints.html'
    form_class = AwardPointsForm

    def get_form_kwargs(self):
        kwargs = super(AddPointsView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs






