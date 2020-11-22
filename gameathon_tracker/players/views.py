from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from django.contrib.auth import authenticate


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('gameboard')

    def get_object(self):
        return self.request.user

