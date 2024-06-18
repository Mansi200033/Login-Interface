from rest_framework import serializers
from src.user.Login.models import Sivista_Users

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Sivista_Users
        fields="__all__"