from django import forms
from .models import Award
from gameboard.models import PlayerGameboard, Gameboard
from django.contrib.auth.models import User

class AwardPointsForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('user')
        super(AwardPointsForm, self).__init__(*args, **kwargs)
        if self.current_user:
            self.fields['player_gameboard_id'].queryset = PlayerGameboard.objects.filter(player_id=self.current_user)



class TestAwardForm(forms.Form):
    gameboard = forms.ModelChoiceField(queryset=Gameboard.objects.none(), label='Gameboard')
    player = forms.ModelChoiceField(queryset=User.objects.all(), label='Player')
    game_name = forms.CharField(label='Game Name', max_length=200)
    position = forms.IntegerField(label='Place')
    team_game = forms.BooleanField(label='Team Game?')
    points_awarded = forms.IntegerField(label='Points')

    def __init__(self, user, *args, **kwargs):
        super(TestAwardForm, self).__init__(*args, **kwargs)
        self.fields['gameboard'] = forms.ModelChoiceField(queryset=Gameboard.objects.filter(gameboard_players=user))


