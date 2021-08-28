from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Poll, Question, Choice, Answer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Poll


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Choice


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class TextAnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer_text',)


class SingleAnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('single_choice',)


class FewAnswersSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('multiple_choice',)
