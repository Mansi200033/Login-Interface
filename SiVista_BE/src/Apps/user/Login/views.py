from rest_framework.views import APIView
from src.Apps.user.Login.serializers import *
from rest_framework import status
from django.http import JsonResponse, HttpResponse,response
from src.Services.LoginService import *
from django.views import View
import json
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrftoken': request.COOKIES['csrftoken']})


"""@api_view(['POST'])
def Login(request):
    
    if request.method == 'POST':
        
            userName=request.data.get('Username').upper()
            password=request.data.get('Password')
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
                    return JsonResponse(response_data)"""
               
                    

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
            
        