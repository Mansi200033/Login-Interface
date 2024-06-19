from src.user.Login.models import *
import hashlib
from src.user.Login.serializers import *
from django.http import JsonResponse, response


def PassCheck(User_details, password):
    
    result = hashlib.md5(password.encode())
    for user in User_details:
        if user.Password==result.hexdigest():
            print('True')
            return True
        else:
            print('False')
            #response_data={"message": "Username and password are invalid."}
            return False
          
          
def CheckUser(user):
    
    filtered_user = User.objects.filter(Usename=user)
    print(type(filtered_user))
    filter_list=list(filtered_user)
    print(filter_list)
    if not filtered_user:
        return filter_list
    else:
        #response_data = {"message": "Invalid credentials","status":401}
        print(filter_list)
        return filter_list

    
def IsActive(user_detail):
    
    for user in user_detail:
        if user.Is_active==True:
            print('True')
            return True
        else:
            print('False')
            return False
   


