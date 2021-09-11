from django.contrib import admin

from store import models

# admin.site.register(models.Category)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated')
    list_filter = ('in_stock', 'is_active')
    list_editable = ('price', 'in_stock')
    prepopulated_fields = {'slug': ('title',)}
