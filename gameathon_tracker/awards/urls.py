from django.urls import path
from .views import AddPointsView


urlpatterns = [
    path('', AddPointsView.as_view(), name='awards'),
]