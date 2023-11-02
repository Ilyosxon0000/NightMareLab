from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("user-types", views.UserTypeViewSet,basename="user-types")
router.register("categories", views.CategoryViewSet,basename="categories")
router.register("subcategories", views.SubCategoryViewSet,basename="subcategories")
router.register("tags",views.TagViewSet,basename="tags")
router.register("bodycategories", views.BodyCategoryViewSet,basename="bodycategories")
router.register("animations", views.AnimationViewSet,basename="animations")
router.register("payment", views.PaymentViewSet,basename="payment")

urlpatterns = [
    path('v1/',include(router.urls)),
]