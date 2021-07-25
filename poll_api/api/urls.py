from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('polls', PollViewSet)
router.register(
    'polls/(?P<id>\d+)/questions',
    QuestionViewSet,
    basename='questions'
)

urlpatterns = [
    path('', include(router.urls)),
]