from rest_framework import serializers
from .models import *


class PollUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PollUser
