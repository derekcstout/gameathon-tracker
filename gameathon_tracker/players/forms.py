from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 max_length=32, label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                max_length=32, label='Last Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=64, label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password Again')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
