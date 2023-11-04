from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model

class UserType(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()#HARDCODE

class UserProfile(AbstractBaseUser):
    image=models.FileField(upload_to="users/%y/%m/%d/",blank=True,null=True)
    middle_name=models.CharField(max_length=255,blank=True,null=True)
    type=models.ForeignKey(UserType,related_name="users",on_delete=models.CASCADE)

    @property
    def owner_animations(self):
        if hasattr(self,'my_owner_animations'):
            return self.my_owner_animations
        return None
    
    @property
    def user_animations(self):
        if hasattr(self,'my_animations'):
            return self.my_animations
        return None
