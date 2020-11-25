#from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('gameboard')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('gameboard')

