from django.db import models
from apps.common.models import BaseModel
# Create your models here.


class HomeSlider(BaseModel):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    image = models.ImageField(upload_to='slider/', verbose_name='Фото')
    short_description = models.CharField(max_length=50, verbose_name='Краткое описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class InstagramPhoto(BaseModel):
    photo = models.ImageField(upload_to='instagram/photo/', verbose_name='Фото на странице')


class WatchOfChoice(BaseModel):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    short_description = models.TextField()
    photo = models.ImageField(upload_to='photos/watches/choices/', verbose_name='Выборы часов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Часы на выбор'
        verbose_name_plural = 'Часы на выбор'
