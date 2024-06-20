from django.urls import path
from src.Apps.user.Login.views import *

urlpatterns = [
    path('login/', Login.as_view(), name='Login'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),

]