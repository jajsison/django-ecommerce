from rest_framework import viewsets
from .models import Product, Banner, Category, Brand
from django.http import HttpResponse, JsonResponse
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework.permissions import DjangoObjectPermissions
from django.db.models import Max, Min
from django.utils.text import slugify
from rest_framework import status
from rest_framework.response import Response


class HomeViewSet(viewsets.ViewSet):

    def get_home(self, request):
        banner = Banner.objects.all().order_by('-id')
        data = Product.objects.filter(is_featured=True).order_by('-id')
        cats = Category.objects.all()
        brands = Brand.objects.all()
        return render(request, 'index.html', {'data': data, 'banner': banner, 'cats': cats, 'brands': brands})


class ProductViewset(viewsets.ViewSet):
    # queryset = Product.objects.all()
    # serializer_class = ProductSerializer

    def get_product_list(self, request,):
        data = Product.objects.all().order_by('-id')
        # check catagory from foregin table
        cats = Product.objects.distinct().values('category__title')
        brands = Product.objects.distinct().values('brand__title')
        return render(request, 'product/product-list.html', {'data': data, 'cats': cats, 'brands': brands, })

    def product_detail(self, request, slug, id):
        product = Product.objects.get(id=id)
        related_products = Product.objects.filter(
            category=product.category).exclude(id=id)[:3]
        return render(request, 'product/product-detail.html', {'product': product, 'related': related_products})

    def category_list(self, request):
        data = Category.objects.all().order_by('-id')
        return render(request, 'category/category-list.html', {'data': data})

    def brand_list(self, request):
        data = Brand.objects.all().order_by('-id')
        return render(request, 'brand/brand-list.html', {'data': data})

    def brand_product_list(self, request, *args, **kwargs):
        brand = Brand.objects.get(id=self.kwargs.get('id'))
        data = Product.objects.filter(brand=brand).order_by('-id')
        cats = Product.objects.distinct().values('category__title')
        brands = Product.objects.distinct().values('brand__title')
        return render(request, 'brand-product-list.html', {'data': data, 'cats': cats, 'brands': brands, })

    def category_product_list(self, request, *args, **kwargs):
        category = Category.objects.get(id=self.kwargs.get('id'))
        data = Product.objects.filter(category=category).order_by('-id')
        cats = Product.objects.distinct().values('category__title')
        brands = Product.objects.distinct().values('brand__title')
        return render(request, 'category/category-product-list.html', {'data': data, 'cats': cats, 'brands': brands, })

    def filter_data(self, request, *args, **kwargs):
        categories = request.GET.getlist('category[]')
        brands = request.GET.getlist('brand[]')
        # minPrice = request.GET['minPrice']
        # maxPrice = request.GET['maxPrice']
        # allProducts = Product.objects.all().order_by('-id').distinct()
        # allProducts = allProducts.filter(productattribute__price__gte=minPrice)
        # allProducts = allProducts.filter(productattribute__price__lte=maxPrice)
        if len(categories) > 0:
            allProducts = allProducts.filter(
                category__id__in=categories).distinct()
        if len(brands) > 0:
            allProducts = allProducts.filter(brand__id__in=brands).distinct()

        t = render_to_string('ajax/product-list.html', {'data': allProducts})
        return JsonResponse({'data': t})

    # def create_product(request):


class CartView(viewsets.ViewSet):

 # Add to cart
    def addCart(self, request):
        cart_p = {}
        cart_p[str(request.GET['id'])] = {
            'image': request.GET['image'],
            'title': request.GET['title'],
            'qty': request.GET['qty'],

            'price': request.GET['price'],
        }
        if 'cartdata' in request.session:
            if str(request.GET['id']) in request.session['cartdata']:
                cart_data = request.session['cartdata']
                cart_data[str(request.GET['id'])]['qty'] = int(
                    cart_p[str(request.GET['id'])]['qty'])
                cart_data.update(cart_data)
                request.session['cartdata'] = cart_data
            else:
                cart_data = request.session['cartdata']
                cart_data.update(cart_p)
                request.session['cartdata'] = cart_data

        else:
            request.session['cartdata'] = cart_p
        return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})

    # Cart List Page

    def cart_list(self, request):
        total_amt = 0
        if 'cartdata' in request.session:
            for p_id, item in request.session['cartdata'].items():
                total_amt += int(item['qty'])*float(item['price'])
            return render(request, 'cart.html', {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']), 'total_amt': total_amt})
        else:
            return render(request, 'cart.html', {'cart_data': '', 'totalitems': 0, 'total_amt': total_amt})

    # Delete Cart Item

    def delete_cart_item(request):
        p_id = str(request.GET['id'])
        if 'cartdata' in request.session:
            if p_id in request.session['cartdata']:
                cart_data = request.session['cartdata']
                del request.session['cartdata'][p_id]
                request.session['cartdata'] = cart_data
        total_amt = 0
        for p_id, item in request.session['cartdata'].items():
            total_amt += int(item['qty'])*float(item['price'])
        t = render_to_string('ajax/cart-list.html', {'cart_data': request.session['cartdata'], 'totalitems': len(
            request.session['cartdata']), 'total_amt': total_amt})
        return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})

# Delete Cart Item


def update_cart_item(request):
    p_id = str(request.GET['id'])
    p_qty = request.GET['qty']
    if 'cartdata' in request.session:
        if p_id in request.session['cartdata']:
            cart_data = request.session['cartdata']
            cart_data[str(request.GET['id'])]['qty'] = p_qty
            request.session['cartdata'] = cart_data
    total_amt = 0
    for p_id, item in request.session['cartdata'].items():
        total_amt += int(item['qty'])*float(item['price'])
    t = render_to_string('ajax/cart-list.html', {'cart_data': request.session['cartdata'], 'totalitems': len(
        request.session['cartdata']), 'total_amt': total_amt})
    return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})


class ProductView(viewsets.ViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = [DjangoObjectPermissions]

    def get(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_product(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        product = Product.objects.get(id=self.kwargs.get('id'))
        serializer = ProductSerializer(
            product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

        # def retrieve(self, request, pk):

    def delete(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        product = Product.objects.get(id=self.kwargs.get('id'))

        product.delete()
        data = {'message': "Successfully submitted from data"}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
        # if self.request.is_ajax():
        #     instance = self.get_object()
        #     self.perform_destroy(instance)
        #     data = {'message': "Successfully submitted from data"}
        #     return JsonResponse(data)
        # return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryView(viewsets.ViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_category(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        product = Product.objects.get(id=self.kwargs.get('id'))
        serializer = ProductSerializer(
            product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


class BrandView(viewsets.ViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_brandview(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        product = Product.objects.get(id=self.kwargs.get('id'))
        serializer = ProductSerializer(
            product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
