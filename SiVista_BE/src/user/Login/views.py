from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from src.user.Login.serializers import *
import json
from rest_framework import status
from django.http import JsonResponse
from src.Services.LoginService import *
from .serializers import UserDetailSerializer

@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        
            userName=request.data.get('Username').upper()
            password=request.data.get('Password').upper()
            print(userName,password)
            User=CheckUser(userName)
            print(User)
            if User:
                isActive=IsActive(User)
                if isActive:
                    passFlag=PassCheck(User,password)
                    if passFlag:
                        response_data={"message":"Success", "status":status.HTTP_200_OK}
                        return JsonResponse(response_data)
                    else:
                        response_data={"message1": "Invalid Credentials.","status":status.HTTP_401_UNAUTHORIZED}
                        return JsonResponse(response_data)      
                else:
                    response_data={"message2": "User not active kindly coordinate with administation group.","status":status.HTTP_401_UNAUTHORIZED}
                    return JsonResponse(response_data)
            else:
                    response_data={"message3": "Invalid Credentials.","status":status.HTTP_401_UNAUTHORIZED}
                    return JsonResponse(response_data)
               
                    
                          
            
            
        