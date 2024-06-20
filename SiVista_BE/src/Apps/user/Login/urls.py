from django.urls import path
from src.Apps.user.Login.views import *

urlpatterns = [
    path('login/', Login.as_view(), name='Login')
]