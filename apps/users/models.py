from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.main.models import BaseModel
# Create your models here.


class CustomUser(AbstractUser):
    pass


class Wishlist(BaseModel):
    user = models.OneToOneField(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    product = models.ManyToManyField('shop.Product', related_name='favs', verbose_name='Избранное')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
