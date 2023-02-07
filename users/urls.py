from django.urls import path, include
from .views import UserView, UserViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="users")


urlpatterns = []
urlpatterns += router.urls
