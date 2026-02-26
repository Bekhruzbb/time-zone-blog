from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']


@admin.register(models.InstagramPhoto)
class InstagramPhotoAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(models.WatchOfChoice)
class WatchOfChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
