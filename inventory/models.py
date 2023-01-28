from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify


# Create your models here.

# Banner
class Banner(models.Model):
    img = models.ImageField(upload_to="banner_imgs/")
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = '1. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text


# Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural = '2. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

# Brand


class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural = '3. Brands'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

# product


class Product(models.Model):
    title = models.CharField(max_length=100)

    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specification = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '4. Product'

    def __str__(self):
        return self.title

# Product Attribute


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)
    image = models.ImageField(upload_to="product_imgs/", null=True)

    class Meta:
        verbose_name_plural = '5. ProductAttributes'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.product.title
