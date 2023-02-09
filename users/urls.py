from django.urls import path, include
from .views import UserViewSet, ProductViewSet, CategoryViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"users", UserViewSet)

router.register(r"products", ProductViewSet)
router.register(r"category", CategoryViewSet)

urlpatterns = []
urlpatterns += router.urls
