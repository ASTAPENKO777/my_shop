from django.shortcuts import render, get_object_or_404

from .models import Product, Order, Category, Customer

def shop_page(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "shop.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)

def index(request):
    context = {"product": "Shop"}
    return render(request, "index.html", context)

def orders(request):
    orders = get_object_or_404(Order)
    context = {"Orders": orders}
    return render(request, "orders.html", context)

def customer(request):
    customers = get_object_or_404(Customer)
    context = {"customers": customers}
    return render(request, "customers.html", context)

def category(request):
    categorys = get_object_or_404(Category)
    context = {"categorys": categorys}
    return render(request, "categorys.html", context)
