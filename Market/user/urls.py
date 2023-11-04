from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("user-types", views.UserTypeViewSet,basename="user-types")

urlpatterns = [
    path('users/',include(router.urls)),
]