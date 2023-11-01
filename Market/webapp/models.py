from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
# Create your models here.

class UserProfile(AbstractBaseUser):
    image=models.FileField(upload_to="users/%y/%m/%d/",blank=True,null=True)
    middle_name=models.CharField(max_length=255,blank=True,null=True)

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
    

class Category(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()

class SubCategory(models.Model):
    category=models.ForeignKey(Category,related_name="subcategories",on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    slug=models.SlugField()

class Tag(models.Model):
    category=models.ForeignKey(Category,related_name="tags",on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory,related_name="tags",on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    slug=models.SlugField()

class BodyCategory(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField()

class Animation(models.Model):
    name=models.CharField(max_length=255)
    file=models.FileField(upload_to="animations/file/%y/%m/%d/")
    tag=models.ForeignKey(Tag,related_name="animations",on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    preview=models.FileField(upload_to="animations/preview/%y/%m/%d/")
    owner=models.ForeignKey(get_user_model(),related_name="my_owner_animations",on_delete=models.PROTECT,blank=True,null=True)
    downloads=models.IntegerField(default=0)
    body_category=models.ForeignKey(BodyCategory,related_name="animations",on_delete=models.CASCADE)

class Payment(models.Model):
    TYPE_PAYMENT=(
        ("TO_COMPANY","TO_COMPANY"),
        ("TO_USER","TO_USER"),
    )
    user=models.ForeignKey(get_user_model(),related_name="my_animations",on_delete=models.PROTECT)
    type_pay=models.CharField(max_length=255,choices=TYPE_PAYMENT,default="TO_COMPANY")
    animation=models.ForeignKey(Animation,related_name="users_animations",on_delete=models.PROTECT)
    amount=models.IntegerField(default=0)
    date_paid=models.DateTimeField(auto_now_add=True)

# TODO