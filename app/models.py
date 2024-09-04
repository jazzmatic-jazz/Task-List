from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom user using AbstractBaseUser where we use
    email field as the main field for login
    fields are:
        - email
        - first_name
        - last_name
        - created_at
        - is_staff
        - is_active
        - is_deleted
    '''    
    email = models.EmailField(max_length=200, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    created_at = models.DateField(auto_now_add=True, editable=False)
    is_staff = models.BooleanField(default=0)
    is_active = models.BooleanField(default=0)
    is_deleted = models.BooleanField(default=0, editable=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()