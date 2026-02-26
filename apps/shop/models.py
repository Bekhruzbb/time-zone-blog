from django.db import models
from apps.common.models import BaseModel
# Create your models here.


class Product(BaseModel):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    short_description = models.CharField(max_length=50, verbose_name='Краткое описание')
    price = models.FloatField(verbose_name='Цена товара: ')
    preview = models.ImageField(upload_to='shop/preview/', verbose_name='Превью')
    slug = models.SlugField(unique=True)
    quantity = models.IntegerField(verbose_name='Кол-во')

    def __str__(self):
        return f'{self.title}'

    def get_price(self):
        return float(self.price)


class ProductPhoto(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт', related_name='photos')
    image = models.ImageField(upload_to='shop/images', verbose_name='Фото')

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'

