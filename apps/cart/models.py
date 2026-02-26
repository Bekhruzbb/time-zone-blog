from django.db import models
from apps.common.models import BaseModel
from apps.shop.models import Product
# Create your models here.


class Cart(BaseModel):
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)

    def get_total_price(self):
        return sum([i.get_total_price() for i in self.cart_products.all()])

    def get_total_quantity(self):
        return sum([i.quantity for i in self.cart_products.all()])

    def get_total_price_without_sale(self):
        return sum([i.get_total_price_discount() for i in self.cart_products.all()])

    def __str__(self):
        return f"{self.user.username}"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, verbose_name='Корзина', related_name='cart_products', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name='Цена', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(verbose_name='Кол-во')

    def get_total_price(self):
        if self.product:
            return self.product.get_price() * self.quantity

    def get_total_price_discount(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = 'Продукт Корзина'
        verbose_name_plural = 'Продукты Корзины'


class Checkout(BaseModel):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    country = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=20)
    address_line2 = models.CharField(max_length=20)
    city = models.CharField(max_length=40)
    district = models.CharField(max_length=30)
    zip = models.IntegerField(max_length=10)
    notes = models.TextField()

    def get_total_price(self):
        return sum([i.get_total_price() for i in self.orders.all()])

    def get_total_quantity(self):
        return sum([i.get_quantity() for i in self.orders.all()])


class OrderItem(BaseModel):
    order = models.ForeignKey(Checkout, verbose_name='Заказ', related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукты', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField(null=True)

    def __str__(self):
        return f'{self.order}'

    def get_quantity(self):
        return self.quantity

    def get_total_price(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

