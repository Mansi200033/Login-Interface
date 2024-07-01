from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    
    name = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=8,unique=True)
    email = models.EmailField(max_length=50, null=False)
    password=models.CharField(max_length=100, null=True)
    is_active =models.BooleanField(default=False, null=False)
    is_staff=models.BooleanField(default=False, null=False, db_column="is_admin")
    first_name=None
    last_name=None
    last_login=None

    USERNAME_FIELD ="username"
    
    objects = UserManager()
    class Meta:
        db_table = "USER"
