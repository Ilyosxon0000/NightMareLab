from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Payment)
admin.site.register(models.RequestType)
admin.site.register(models.Request)
admin.site.register(models.Company)