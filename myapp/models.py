from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from uuid import uuid4

# Create your models here.
class organisation(models.Model):
    org_name = models.CharField(max_length=100)
    org_desc = models.TextField(blank=True, null=True)
    org_logo = models.ImageField(upload_to='org_logo')
    org_page = models.CharField(max_length=200)

    def __str__(self):
        return self.org_name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(unique=True, editable=False, default=uuid4)
    email = models.EmailField(max_length=200, null=True, blank=True)
    user_name = models.CharField(max_length=30, unique=True, blank=True)
    user_pass = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_employee = models.BooleanField('Is_employee', default=False, null=True)
    user_pic = models.ImageField(upload_to='user_pic', null=True, blank=True)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['is_employee', 'user_pic']

    objects = CustomUserManager()

    def __str__(self):
        return self.user_name