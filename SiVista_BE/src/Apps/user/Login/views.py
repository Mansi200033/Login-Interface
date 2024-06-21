from rest_framework.views import APIView
from rest_framework import status
import json
from django.http import JsonResponse
from src.Services.LoginService import *
from src.Models.Login.LoginResponse import *
from src.Apps.user.Login.models import User
from src.Apps.user.Login.serializers import *


class Login(APIView):
    def post(self, request,format=None):
        data = json.loads(request.body)
        userName=data['Username']
        password=data['Password']
        User=CheckUser(userName)
        if User:
            isActive=IsActive(User)
            if isActive:
                passFlag=PassCheck(User,password)
                if passFlag:
                    message='Success'
                    responseStatus=status.HTTP_200_OK
                    return JsonResponse(vars(LoginResponse(message,responseStatus)))  
                else:
                    message='Invalid Credentials.'
                    responseStatus=status.HTTP_401_UNAUTHORIZED
                    return JsonResponse(vars(LoginResponse(message,responseStatus)))      
            else:
                message='User not active kindly coordinate with administration group.'
                responseStatus=status.HTTP_401_UNAUTHORIZED
                return JsonResponse(vars(LoginResponse(message,responseStatus)))    
            
        else:
            message='Invalid Credentials.'
            responseStatus=status.HTTP_401_UNAUTHORIZED
            return JsonResponse(vars(LoginResponse(message,responseStatus)))  
                           
            
        