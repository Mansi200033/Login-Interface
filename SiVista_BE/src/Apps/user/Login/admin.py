from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from src.Apps.user.Login.models import User
# Register your models here.

admin.site.register(User)