from django.urls import include, path

from . import views
from rest_framework import routers
from .views import LoginView, RegisterView, CreateUserViewSet, LoginViewSet


urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register2/',
         CreateUserViewSet.as_view({'post': 'create'}), name='register2'),
    path('login2/',
         LoginViewSet.as_view({'get': 'get'}), name='login2'),
]
