from django.urls import path
from .views import AddPointsView, load_players, test


urlpatterns = [
    path('', AddPointsView.as_view(), name='awards'),
    path('test/load_players/', load_players, name='load_players'),
    path('test/', test, name='test'),
]