from django.contrib import admin
from .models import Category, Brand, Product, ProductAttribute, Banner

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product)
admin.site.register(Brand)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')


admin.site.register(Banner, BannerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category',
                    'brand', 'status', 'is_featured')
    list_editable = ('status', 'is_featured')


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'product', 'price')


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductAttribute, ProductAttributeAdmin)

# admin.site.register(Item)
# admin.site.register(Order)
# admin.site.register(OrderItems)
# admin.site.register(ColorVariant)
# admin.site.register(SizeVariant)
# admin.site.register(ProductImages)
