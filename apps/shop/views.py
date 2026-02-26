from django.shortcuts import render
from . import models
# Create your views here.


def show_shop_page(request):
    products = models.Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'shop/shop.html', context)


def show_product_page(request, slug):
    product = models.Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'shop/products.html', context)