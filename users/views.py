from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated


from django.contrib.auth import login, authenticate
from rest_framework.decorators import action
from knox.views import LoginView as knox_views

from django.contrib import messages

# Create your views here.


class LoginView(TemplateView):
    template_name = 'users/login.html'


class RegisterView(TemplateView):
    template_name = 'users/register.html'
