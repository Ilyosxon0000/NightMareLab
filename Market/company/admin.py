from django.contrib import admin
from . import models

admin.site.register(models.RequestType)
admin.site.register(models.Request)
admin.site.register(models.Company)
