from django.urls import path
from .views import load_players, award_points


urlpatterns = [
    path('', award_points, name='awards'),
    path('load_players/', load_players, name='load_players'),
]