from rest_framework.generics import get_object_or_404

from .serializers import *
from rest_framework import viewsets

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        parent_poll = get_object_or_404(Poll, id=self.kwargs['id'])
        return parent_poll.questions.all()

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, pk=self.kwargs['id'])
        serializer.save(parent_poll=poll)

