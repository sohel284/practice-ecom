from django.contrib import admin

from product.models import Product
from product.models import ProductRating


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRating, ProductAdmin)
