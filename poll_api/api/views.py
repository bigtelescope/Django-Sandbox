from rest_framework.generics import get_object_or_404

from .serializers import *
from rest_framework import viewsets, permissions


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAdminUser,)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        parent_poll = get_object_or_404(Poll, id=self.kwargs['id'])
        return parent_poll.questions.all()

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, pk=self.kwargs['id'])
        serializer.save(parent_poll=poll)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        parent_question = get_object_or_404(
            Question,
            id=self.kwargs['question_id'],
        )
        return parent_question.choices.all()

    def perform_create(self, serializer):
        parent_question_ = get_object_or_404(Question, pk=self.kwargs['question_id'])
        serializer.save(parent_question=parent_question_)
