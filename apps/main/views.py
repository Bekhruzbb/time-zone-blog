from django.shortcuts import render
from apps.main.models import HomeSlider, WatchOfChoice, InstagramPhoto
from apps.cart.models import Cart
from apps.shop.models import Product, ProductPhoto
# Create your views here.


def show_home_page(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)

    slides = HomeSlider.objects.all()
    images = InstagramPhoto.objects.all()
    watchofchoices = WatchOfChoice.objects.all()
    products = Product.objects.all()
    context = {
        'slides': slides,
        'images': images,
        'watchofchoices': watchofchoices,
        'products': products
    }

    return render(request, 'main/index.html', context)


def show_contacts_page(request):
    return render(request, 'main/contacts.html')