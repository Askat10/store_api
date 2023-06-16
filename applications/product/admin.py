from django.contrib import admin

from applications.product.models import Product, ProductImage


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine]
