from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from src.user.Login.views import *

routers=routers.DefaultRouter()
routers.register(r'saveuser',Login_User)



urlpatterns = [
    path('', include(routers.urls)),
    path('http://localhost:3000', Login, name='Login'),
   
]