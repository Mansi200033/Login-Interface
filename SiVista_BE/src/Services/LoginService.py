from src.user.Login.models import *
import hashlib
from src.user.Login.serializers import *
from django.http import HttpResponse

def PassCheck(User_details, password):

    result = hashlib.md5(password.encode())
    for user in User_details:
        if user.Password==result.hexdigest():
            return True
        else:
            return HttpResponse({"message": "Username and password are invalid."})
        

def CheckUser(user):
    try:
        filtered_user = Sivista_Users.objects.filter(Usename=user)
        filter_list=list(filtered_user)
        print(filter_list)
        return filter_list
    except Exception as e:
        print(e)

def IsActive(user_detail):
    for user in user_detail:
        if user.Is_active==True:
            return True
        else:
            return HttpResponse({"message": "User not active kindly coordinate with administation group."})
        