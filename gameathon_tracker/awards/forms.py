from django import forms
from gameboard.models import PlayerGameboard, Gameboard
from django.contrib.auth.models import User


class AwardForm(forms.Form):
    gameboard = forms.ModelChoiceField(queryset=Gameboard.objects.none(),
                                       label='Choose Gameboard',
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    player = forms.ModelChoiceField(queryset=User.objects.none(),
                                    label='Player:',
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    game_name = forms.CharField(label='What game did you play?',
                                max_length=200,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.IntegerField(label='Place #',
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    team_game = forms.BooleanField(label='Team Game?',
                                   required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    points_awarded = forms.IntegerField(label='Points',
                                        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def __init__(self, user, *args, **kwargs):
        super(AwardForm, self).__init__(*args, **kwargs)
        self.fields['gameboard'] = forms.ModelChoiceField(queryset=Gameboard.objects.filter(gameboard_players=user),
                                                          label='Choose Gameboard',
                                                          widget=forms.Select(attrs={'class': 'form-control'}))


