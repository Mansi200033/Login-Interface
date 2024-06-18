from django.shortcuts import render, HttpResponse, redirect
from src.user.Login.models import *
import hashlib
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from src.user.Login.serializers import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from src.Services.LoginService import *

@csrf_exempt
def Login(request):
    if request.method== 'POST':
        try:
            data=json.loads(request.body)
            print(data)
            userName=data.get('Username').upper()
            password=data.get('Password').upper()
            print(userName,password)
            User=CheckUser(userName)
            print(User)
            IsActive(User)
            PassCheck(User,password)
            return HttpResponse("Success")
        except Exception as e:
            print(e)
            render ('http://localhost:3000/')

def login1(request):
    HttpResponse("Hii Team")


class Login_User(viewsets.ModelViewSet):
    queryset= Sivista_Users.objects.all()
    serializer_class=UserDetailSerializer



