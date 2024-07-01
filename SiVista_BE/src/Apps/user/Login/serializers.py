from rest_framework import serializers
from src.Apps.user.Login.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from src.Services.LoginService import *

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields="__all__"

class LoginSerializer(serializers.Serializer):
    Username=serializers.CharField(max_length=8)
    Password=serializers.CharField(max_length=100)

    def validate(self,data):
        user=CheckUser(data['Username'].upper())
        if user and PassCheck(user,data['Password']):
            if IsActive(user):
                message='Success'
                responseStatus=status.HTTP_200_OK
                return message,responseStatus,user
            else:
                message=f'User {data['Username'].upper()} is inactive, kindly coordinate with Admin user.'
                responseStatus=status.HTTP_401_UNAUTHORIZED
                return message,responseStatus,user
        else:
            message='Invalid Credentials'
            responseStatus=status.HTTP_401_UNAUTHORIZED
            return message, responseStatus,user
    
    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

            