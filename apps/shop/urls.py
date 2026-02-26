from . import views
from django.urls import path
app_name = 'shop'

urlpatterns = [
    path('', views.show_shop_page, name='shop'),
    path('product/<slug:slug>', views.show_product_page, name='detail')
]