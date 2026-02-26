from . import views
from django.urls import path
app_name = 'cart'

urlpatterns = [
    path('', views.show_cart_page, name='cart'),
    path('checkout/', views.show_checkout_page, name='checkout'),
    # add
    path('cart/<str:product_id>/<int:quantity>/', views.add_cart_products, name='add-cart'),
    # delete
    path('cart/<str:product_id>/', views.delete_cart_products, name='delete-cart'),

    path('checkout-add/', views.checkout_view, name='check-add'),
    path('thank-you/<str:order_id>', views.show_thank_page, name='thank')
]