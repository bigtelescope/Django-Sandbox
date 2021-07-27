from rest_framework import serializers
from .models import Poll, Question, Choice


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
