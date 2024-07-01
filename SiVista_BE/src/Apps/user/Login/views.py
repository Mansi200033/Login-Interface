from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from src.Models.Login.LoginResponse import *
from src.Apps.user.Login.serializers import *


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
            return JsonResponse(data)
        except Exception as e:
            print(e)
