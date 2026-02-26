from django.contrib import admin
from . import models
# Register your models here.


class InstagramPhotoInline(admin.TabularInline):
    model = models.InstagramPhoto
    extra = 1


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'created_at']
    list_display_links = ['title']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title']
    list_display_links = ['title']


@admin.register(models.InstagramPhoto)
class InstagramPhoto(admin.ModelAdmin):
    list_display = ['id']
