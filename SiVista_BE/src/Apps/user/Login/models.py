from django.db import models

# Create your models here.
class User(models.Model):
    
    Name = models.CharField(max_length=100, null=False)
    Username = models.CharField(max_length=100, null=False)
    Email = models.EmailField(max_length=100, null=False)
    Password=models.CharField(max_length=200, null=False)
    Is_active =models.BooleanField(default=False, null=False)
    Is_admin=models.BooleanField(default=False, null=False)

    class Meta:
        db_table = "USER"
