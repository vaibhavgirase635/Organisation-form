from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, user_name, user_pass, is_employee, user_pic, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not user_name:
            raise ValueError(_('Users must have an email address'))
        if not user_pass:
            raise ValueError(_('Users must have an email password'))
        
        
        user = self.model(user_name=user_name, is_employee=is_employee, user_pic=user_pic, **extra_fields)
                          
                          
                          
        user.set_password(user_pass)
        user.save()
        return user

    def create_superuser(self,user_name,is_employee, user_pic, password=None):
        user=self.create_user(
            
            user_pass=password,
            user_name=user_name,
            is_employee=is_employee,
            user_pic=user_pic
        )
        user.is_superuser=True
        user.is_staff=True
        user.is_active=True
        user.save(using=self._db)
        return user