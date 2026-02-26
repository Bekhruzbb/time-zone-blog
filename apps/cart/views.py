from django.shortcuts import render, redirect
from apps.cart.models import Cart, CartItem, Checkout, OrderItem
from apps.shop.models import Product
from .forms import BillingForm


# Create your views here.


def add_cart_products(request, product_id, quantity):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=product_id)
    if product in [i.product for i in cart.cart_products.all()]:
        product_cart = CartItem.objects.get(product=product)
        product_cart.quantity += quantity
        product.quantity -= quantity
        product_cart.save()
        cart.save()
    else:
        CartItem.objects.create(product=product, quantity=quantity, cart=cart)
        product.quantity -= quantity
        product.save()
    return redirect('cart:cart')


def delete_cart_products(request, product_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = cart.cart_products.filter(id=product_id).first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart:cart')


def show_cart_page(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart
    }

    return render(request, 'cart/cart.html', context)


def show_checkout_page(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    form = BillingForm(data=request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('cart:thank')
    else:
        form = BillingForm()
    order = Checkout.objects.all()
    context = {
        'form': form,
        'cart': cart,
        'order': order
    }
    return render(request, 'cart/checkout.html', context)


def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    order = Checkout.objects.create(
        user=request.user,
        first_name=request.POST.get('first_name'),
        last_name=request.POST.get('last_name'),
        company_name=request.POST.get('company_name'),
        phone_number=request.POST.get('phone_number'),
        email_address=request.POST.get('email_address'),
        country=request.POST.get('country'),
        address_line1=request.POST.get('address_line1'),
        address_line2=request.POST.get('address_line2'),
        city=request.POST.get('city'),
        district=request.POST.get('district'),
        zip=request.POST.get('zip'),
        notes=request.POST.get('notes')
    )
    for cart_products in cart.cart_products.all():
        OrderItem.objects.create(
            order=order,
            product=cart_products.product,
            quantity=cart_products.quantity,
            price=cart_products.product.price
        )
    cart.cart_products.all().delete()
    return redirect('cart:thank', order_id=order.id)


def show_thank_page(request, order_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    order = Checkout.objects.get(id=order_id, user=request.user)
    cart_products = order.orders.all()
    total_quan = sum(i.quantity for i in cart_products)
    total_sum = sum(i.price for i in cart_products)
    context = {
        'cart': cart,
        'cart_products': cart_products,
        'total_quan': total_quan,
        'total_sum': total_sum
    }
    return render(request, 'cart/thank-you_page.html', context)
