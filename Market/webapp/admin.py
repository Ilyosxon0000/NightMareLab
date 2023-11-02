from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.BodyCategory)
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.Tag)
admin.site.register(models.Animation)
admin.site.register(models.Payment)
admin.site.register(models.RequestType)
admin.site.register(models.Request)
admin.site.register(models.Company)