from django.urls import include, path

from . import views
from rest_framework import routers
from .views import LoginView, RegisterView
from .api import CreateUserViewSet, LoginViewSet, LogoutViewSet

app_name = 'users'
urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register2/',
         CreateUserViewSet.as_view({'post': 'create'}), name='register2'),
    #     path('register3/',
    #          CreateUserViewSet.as_view({'post': 'registration'}), name='register3'),
    path('login2/',
         LoginViewSet.as_view({'post': 'post'}), name='login2'),
    path('logout/', LogoutViewSet.as_view({'post': 'post'}), name='logout'),
]
