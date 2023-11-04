from django.contrib import admin
from . import models

admin.site.register(models.UserType)
admin.site.register(models.UserProfile)