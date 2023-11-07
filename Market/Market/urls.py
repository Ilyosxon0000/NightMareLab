from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .conf.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('finance.urls')),
    path('api/v1/',include('product.urls')),
    path('api/v1/',include('user.urls')),
    path('api/v1/',include('company.urls')),
]+static(settings.MEDIA_URL,serve,document_root=settings.MEDIA_ROOT)

from django.core.files.storage import Storage
