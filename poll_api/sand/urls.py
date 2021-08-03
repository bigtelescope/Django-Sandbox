from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('login', UserViewSet)

urlpatterns = [
    path('',  include(router.urls)),
]