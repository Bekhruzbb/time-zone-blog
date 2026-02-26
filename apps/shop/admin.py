from django.contrib import admin
from . import models
# Register your models here.


class ProductPhotoInline(admin.TabularInline):
    model = models.ProductPhoto
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']

    inlines = [ProductPhotoInline]


