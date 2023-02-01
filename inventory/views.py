from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework.response import Response

from django.utils.text import slugify

from .models import Category, Product, Banner, Brand
# from .serializers import CategorySerializer, ProductSerializer

from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

# search


def search(request):
    q = request.GET.get('q')
    data = Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request, 'search.html', {'data': data})
