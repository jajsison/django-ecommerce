from rest_framework import viewsets

from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer, RegistrationSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny
from django.contrib import messages


class CreateUserViewSet(viewsets.ViewSet):
    """
    A viewset for creating a new user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    # def register(self, request):
    #     return render(request, 'users/register.html')

    def create(self, *args, **kwargs):

        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            user = serializer.save()
            # login(self.request, user)
            return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def registration(request):

        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                account = serializer.save()
                data['response'] = "Successfully registered a new user."
                data['email'] = account.email
            else:
                data = serializer.errors
            return Response(data)


class LoginViewSet(viewsets.ViewSet):

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validate_login(request.data)
            login(request, user)
            return Response(None, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutViewSet(viewsets.ViewSet):

    def post(self, request):
        logout(request)
        data = {'message': 'Logout successfully'}
        return Response(data=data, status=status.HTTP_202_ACCEPTED)
