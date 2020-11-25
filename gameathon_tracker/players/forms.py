from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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


class EditProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 max_length=32, label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                max_length=32, label='Last Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=64, label='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                   label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                    max_length=32, label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
                                    max_length=32, label='New Password Again')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
