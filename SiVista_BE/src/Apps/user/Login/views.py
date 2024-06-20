from rest_framework.views import APIView
from rest_framework import status
import json
from django.http import JsonResponse
from src.Services.LoginService import *



class Login(APIView):
    
    def post(self, request,format=None):
        print(request)
        data = json.loads(request.body)
        userName=data['Username']
        password=data['Password']
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
                    response_data={"message": "Invalid Credentials.","status":status.HTTP_401_UNAUTHORIZED}
                    return JsonResponse(response_data)      
            else:
                response_data={"message": "User not active kindly coordinate with administation group.","status":status.HTTP_401_UNAUTHORIZED}
                return JsonResponse(response_data)
        else:
                response_data={"message": "Invalid Credentials.","status":status.HTTP_401_UNAUTHORIZED}
                return JsonResponse(response_data)                 
            
        