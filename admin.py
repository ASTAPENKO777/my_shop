from django.contrib import admin

from .models import Product, Category, Customer, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image")
    fields = ("name", "price", "image")


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)

# admin
# password123
