from django.urls import path
from src.Apps.user.Login.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', Login.as_view(), name='Login'),
    path('a1/', home.as_view(), name='Home'),
]