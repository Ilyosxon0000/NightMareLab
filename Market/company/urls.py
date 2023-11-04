from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("request-type", views.RequestTypeViewSet,basename="request-type")
router.register("request", views.RequestViewSet,basename="request")
router.register("company", views.CompanyViewSet,basename="company")

urlpatterns = [
    path('company/',include(router.urls)),
]