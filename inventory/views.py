from django.shortcuts import render

from rest_framework import viewsets

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

from django.views.generic import TemplateView
# Create your views here.


def store(request):
    context = {}
    return render(request, 'store.html', context)


class StoreView(TemplateView):
    template_name = 'store.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class CheckoutView(TemplateView):
    template_name = 'checkout.html'


class CategoryViewSet(viewsets.ViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
