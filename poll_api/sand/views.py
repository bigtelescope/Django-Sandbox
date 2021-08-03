from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import viewsets
from .models import *
from .serializers import *
from ..account.forms import LoginForm


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect("/account/me/")
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/")


class UserViewSet(viewsets.ModelViewSet):
    queryset = PollUser.objects.all()
    serializer_class = PollUserSerializer

    def perform_create(self, serializer):
        potential_user = self.request.data['username']
        potential_passwd = self.request.data['password']
        # user_email = potential_user = self.request.data['email']
        user = auth.authenticate(username=potential_user, password=potential_passwd)
        serializer.save()
