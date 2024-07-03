from rest_framework.views import APIView
from rest_framework import status
import jwt
from django.http import JsonResponse
from rest_framework.response import Response
from src.Services.LoginService import *
from src.Models.Login.LoginResponse import *
from src.Apps.user.Login.models import User
from src.Apps.user.Login.serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import time



class Login(APIView):
    def post(self, request,format=None):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                message,responseStatus ,user= serializer.validated_data
                if responseStatus==200: 
                    token = serializer.get_token(user)
                    #decode_token=jwt.decode(token['access'])
                    #print(decode_token)
                    return JsonResponse(vars(LoginResponse(message,responseStatus,token)))
                else:
                    return JsonResponse(vars(LoginResponse(message,responseStatus)))
            else:
                message="Invalid Credentials."
                responseStatus=status.HTTP_401_UNAUTHORIZED
                return JsonResponse(vars(LoginResponse(message,responseStatus)))
        except Exception as e:
            print(e)


class home(APIView):
   def post(self,request,format=None):
        try:
            print("___start___")
            data=request.data
            print(time.time())
            return JsonResponse({"time":time.time()})
        except Exception as e:
            print(e)


"""class Login(APIView):
    def post(self, request,format=None):
        data = json.loads(request.body)
        userName=data['Username']
        password=data['Password']
        User=CheckUser(userName)
        if User:
            isActive=IsActive(User)
            if isActive:
                passFlag=PassCheck(request,userName,password)
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
                           
       """     
        