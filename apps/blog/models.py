from django.db import models
from apps.common.models import BaseModel

# Create your models here.


class Tag(BaseModel):
    title = models.CharField(verbose_name='Тег', max_length=15)
    slug = models.SlugField(unique=True, verbose_name='Краткая ссылка')

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=20, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Blog(BaseModel):
    preview = models.ImageField(upload_to='blog/preview/', verbose_name='Фото')
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    short_description = models.CharField(max_length=50, verbose_name='Краткое описание')
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='blog/photos', verbose_name='Фото')
    tag = models.ManyToManyField(Tag, verbose_name='Тэг блога', related_name='tags')
    category = models.ManyToManyField(Category, verbose_name='Категория блога', related_name='categories')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница блога'
        verbose_name_plural = 'Страницы блога'


class Comment(BaseModel):
    article = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.TextField()
    name = models.ForeignKey('users.CustomUser', verbose_name='Автор комментария', on_delete=models.CASCADE)
    email = models.EmailField()
    website = models.CharField(max_length=20)


class InstagramPhoto(BaseModel):
    image = models.ImageField(upload_to='blog/photos/', verbose_name='Фото')
