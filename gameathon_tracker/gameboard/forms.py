from django import forms
from .models import Gameboard


class GameboardForm(forms.ModelForm):
    gameboard_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Gameboard
        fields = ('gameboard_name',)


class SearchGameboard(forms.Form):
    q = forms.CharField(label='Search', max_length=200)




