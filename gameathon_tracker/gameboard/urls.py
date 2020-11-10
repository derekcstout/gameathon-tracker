from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gameboard/', views.gameboard, name='gameboard'),
    path('standings/', views.standings, name='standings'),
]