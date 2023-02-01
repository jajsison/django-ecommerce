from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .api import ProductViewset, HomeViewSet, ProductView, CategoryView
from .api import ProductView, CategoryView, BrandView, CartView
from . import views
from rest_framework import routers


from . import views


router = routers.DefaultRouter()
# router.register(r'product_view', ProductView)
# router.register(r'category_view', CategoryView)

urlpatterns = [
    path('', HomeViewSet.as_view({'get': 'get_home'}), name='store'),
    path('search/', views.search, name='search'),
    #     path('api/', include(router.urls)),
    path('product-list/',
         ProductViewset.as_view({'get': 'get_product_list'}), name='product-list'),
    path('product/<str:slug>/<int:id>/',
         ProductViewset.as_view({'get': 'product_detail'}), name='product_detail'),
    path('brand-list/',
         ProductViewset.as_view({'get': 'brand_list'}), name='brand-list'),
    path('brand-product-list/<int:id>/',
         ProductViewset.as_view({'get': 'brand_product_list'}), name='brand-product-list'),
    path('category-list/',
         ProductViewset.as_view({'get': 'category_list'}), name='category-list'),
    path('category-product-list/<int:id>/',
         ProductViewset.as_view({'get': 'category_product_list'}), name='category-product-list/'),
    path('filter-data/',
         ProductViewset.as_view({'get': 'filter_data'}), name='filter-data'),

    # CART
    path('add-to-cart/',
         CartView.as_view({'get': 'addCart'}), name='add-to-cart'),
    path('cart/',
         CartView.as_view({'get': 'cart_list'}), name='cart'),

    # API methods
    path('api-product/',
         ProductView.as_view({'get': 'get', 'post': 'create'}), name='api-product'),
    path('api-product/<int:id>/',
         ProductView.as_view({'post': 'update_product', 'destroy': 'delete'}), name='api-product'),

    path('api-category/',
         CategoryView.as_view({'get': 'get', 'post': 'create'}), name='api-category'),


    path('api-brand/',
         CategoryView.as_view({'get': 'get', 'post': 'create'}), name='api-brand'),






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
