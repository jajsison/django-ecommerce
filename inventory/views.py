from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework.response import Response

from django.utils.text import slugify

from .models import Category, Product, Banner, Brand
# from .serializers import CategorySerializer, ProductSerializer

from django.views.generic import TemplateView
# Create your views here.
