from datetime import datetime

from django.http import HttpResponse
from rest_framework.generics import get_object_or_404

from .models import Answer
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


class ActivePollsViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.raw(
        "SELECT * FROM api_poll WHERE start_data <= %s AND end_data >= %s",
        [datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%Y-%m-%d')]
    )
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated, )


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_serializer_class(self):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_id'],
        )

        if question.question_type == 'TF':
            return TextAnswerSerializer
        elif question.question_type == 'SV':
            return SingleAnswerSerializer
        elif question.question_type == 'FV':
            return FewAnswersSerializer

    def perform_create(self, serializer):
        user = self.request.user
        parent_question_ = get_object_or_404(
            Question,
            pk=self.kwargs['question_id'],
        )
        parent_poll_ = get_object_or_404(
            Poll,
            pk=self.kwargs['id'],
        )

        serializer.save(
                author=user,
                parent_question=parent_question_,
                parent_poll=parent_poll_
        )


def AnswerView(request, id, question_id):
    variants = Choice.objects.raw(
        "SELECT * FROM api_choice WHERE parent_question_id = %s",
        ["1"]
    )
    return HttpResponse(variants)
