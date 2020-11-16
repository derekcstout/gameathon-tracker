from django.urls import path

from . import views
from .views import GameboardSearchResults, GameboardSearch

urlpatterns = [
    path('', views.index, name='index'),
    path('gameboard/', views.gameboard, name='gameboard'),
    path('standings/', views.standings, name='standings'),
    path('gameboard/new/', views.NewGameboard.as_view(), name='newgameboard'),
    path('gameboard/search/results/', GameboardSearchResults.as_view(), name='search_results'),
    path('gameboard/search/', GameboardSearch.as_view(), name='search'),
]