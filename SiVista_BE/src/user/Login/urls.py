from django.urls import path
from src.user.Login.views import Login

urlpatterns = [
    path('login/', Login, name='Login'),
]