from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserEditView, PasswordsChangeView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
]