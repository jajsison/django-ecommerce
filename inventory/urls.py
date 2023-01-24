from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet, StoreView, CartView, CheckoutView
from . import views

router = routers.DefaultRouter()
router.register(r'category_product', CategoryViewSet)
router.register(r'product_item', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('', views.store, name="store"),
    path('', StoreView.as_view(), name='store'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
