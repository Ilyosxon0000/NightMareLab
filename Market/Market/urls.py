from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('finance.urls')),
    path('api/v1/',include('product.urls')),
    path('api/v1/',include('user.urls')),
    path('api/v1/',include('company.urls')),
]

