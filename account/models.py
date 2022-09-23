import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomerUserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,unique=True,blank=False,null=False)
    mobile=models.CharField(max_length=10,blank=True,null=True)
    status = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomerUserManager()

class Book(models.Model):
    book_name = models.CharField(max_length=100,blank=True,null=True)
    book_photo = models.ImageField(upload_to='image/',blank=True, null=True)
    book_title = models.CharField(max_length=300,blank=True,null=True)
    book_author = models.CharField(max_length=100,blank=False, null=False)
    publish_date = models.DateField(default=datetime.date.today())
    total_quantity = models.BigIntegerField()
    available_quantity = models.BigIntegerField(blank=True,null=True)

    def __str__(self):
        return super().__str__()