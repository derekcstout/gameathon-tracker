from django.urls import path
from .views import AddPointsView, runajax, test


urlpatterns = [
    path('', AddPointsView.as_view(), name='awards'),
    path('test/runajax/', runajax, name='runajax'),
    path('test/', test, name='test'),
]