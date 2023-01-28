from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category, Product, Banner, Brand
# from .serializers import CategorySerializer, ProductSerializer

from django.views.generic import TemplateView
# Create your views here.


def home(request):
    banner = Banner.objects.all().order_by('-id')
    data = Product.objects.filter(is_featured=True).order_by('-id')
    return render(request, 'index.html', {'data': data, 'banner': banner})


def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'category-list.html', {'data': data})


def brand_list(request):
    data = Brand.objects.all().order_by('-id')
    return render(request, 'brand-list.html', {'data': data})


def product_list(request):
    data = Product.objects.all().order_by('-id')
    # check catagory from foregin table
    cats = Product.objects.distinct().values('category__title')
    brands = Product.objects.distinct().values('brand__title')
    return render(request, 'product-list.html', {'data': data, 'cats': cats, 'brands': brands, })

# product list according to category


def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.filter(category=category).order_by('-id')
    cats = Product.objects.distinct().values('category__title')
    brands = Product.objects.distinct().values('brand__title')
    return render(request, 'category-product-list.html', {'data': data, 'cats': cats, 'brands': brands, })


def brand_product_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    data = Product.objects.filter(brand=brand).order_by('-id')
    cats = Product.objects.distinct().values('category__title')
    brands = Product.objects.distinct().values('brand__title')
    return render(request, 'brand-product-list.html', {'data': data, 'cats': cats, 'brands': brands, })


def product_detail(request, slug, id):
    product = Product.objects.get(id=id)
    return render(request, 'product-detail.html', {'data': product})
