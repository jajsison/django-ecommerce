from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from rest_framework.response import Response

from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

from django.contrib.auth import login, authenticate

from .models import CustomUser

from knox import views as knox_views
from django.contrib.auth import login

from rest_framework import viewsets
from rest_framework import status

from rest_framework.decorators import action
from knox.views import LoginView as knox_views
# Create your views here.


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class CreateUserViewSet(viewsets.ViewSet):
    """
    A viewset for creating a new user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request):

        if request.method == 'POST':
            serialiazer = UserSerializer(request.POST)
            if UserSerializer.is_valid():
                UserSerializer.save()
                username = UserSerializer.cleaned_data.get('username')
                pwd = serialiazer.cleaned_data.get('password')
                user = authenticate(username=username, password=pwd)
                login(request, user)
                return redirect('register.html')

            serializer = UserSerializer
            return render(request, 'register.html', {'serializer': serializer})

        # """Create a new user"""

        # serializer = UserSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ViewSet):
    permission_classes = AllowAny,

    def get(self, request, format=None):
        import pdb
        pdb.set_trace()
        serializer = LoginSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
