from django.contrib import admin
from .models import Category, Brand, Product, Banner, CartOrder, CartOrderItems

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Brand, BrandAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')


admin.site.register(Banner, BannerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'price', 'category',
                    'brand', 'status', 'is_featured')
    list_editable = ('status', 'is_featured')


admin.site.register(Product, ProductAdmin)


# Order
class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ('paid_status', 'order_status')
    list_display = ('user', 'total_amt', 'paid_status',
                    'order_dt', 'order_status')


admin.site.register(CartOrder, CartOrderAdmin)


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'item', 'image_tag', 'qty', 'price', 'total')


admin.site.register(CartOrderItems, CartOrderItemsAdmin)
