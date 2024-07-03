
import hashlib
from src.Apps.user.Login.models import User

from django.contrib.auth import authenticate



def PassCheck(User, password):
    #return authenticate(request,username=User, password=password)
    result = hashlib.md5(password.encode())
    if User.password==result.hexdigest().upper():
        
        return True
    else:
        
        return False
          
          
def CheckUser(user):
    
    filtered_user = User.objects.filter(username=user).first()
    return filtered_user
    
def IsActive(user):
    return user.is_active
   


