from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('polls', PollViewSet)
router.register('active_polls', ActivePollsViewSet)

router.register(
    'polls/(?P<id>\d+)/questions',
    QuestionViewSet,
    basename='questions'
)

router.register(
    'polls/(?P<id>\d+)/questions/(?P<question_id>\d+)/choices',
    ChoiceViewSet,
)

# router.register(
#     'polls/(?P<id>\d+)/questions/(?P<question_id>\d+)/answer',
#     AnswerView,
#     basename="answer"
# )

urlpatterns = [
    path('', include(router.urls)),
    re_path(
        'polls/(?P<id>\d+)/questions/(?P<question_id>\d+)/answer',
        AnswerView
    )
]