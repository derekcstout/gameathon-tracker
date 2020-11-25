from django.urls import path
from . import views
from .views import GameboardSearchResults, GameboardSearch, JoinGameboard

urlpatterns = [
    path('', views.gameboard, name='gameboard'),
    path('standings/', views.standings, name='standings'),
    path('gameboard/new/', views.NewGameboard.as_view(), name='newgameboard'),
    path('gameboard/search/results/', GameboardSearchResults.as_view(), name='search_results'),
    path('gameboard/search/', GameboardSearch.as_view(), name='search'),
    path('gameboard/joingame/', JoinGameboard, name='join_gameboard'),
    path('gameboard/getscores/', views.load_scores, name='load_scores'),
    path('gameboard/getpieces/', views.load_pieces, name='load_pieces'),
]
