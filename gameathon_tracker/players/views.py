from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


