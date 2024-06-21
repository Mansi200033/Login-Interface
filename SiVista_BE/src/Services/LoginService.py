
import hashlib
from src.Apps.user.Login.models import User
from src.Apps.user.Login.serializers import *



def PassCheck(User_details, password):
    
    result = hashlib.md5(password.encode())
    for user in User_details:
        if user.Password==result.hexdigest():
            
            return True
        else:
            
            return False
          
          
def CheckUser(user):
    
    filtered_user = User.objects.filter(Username=user)
    
    filter_list=list(filtered_user)
    
    if not filtered_user:
        return filter_list
    else:
        
        return filter_list

    
def IsActive(user_detail):
    
    for user in user_detail:
        if user.Is_active==True:
            
            return True
        else:
            
            return False
   


