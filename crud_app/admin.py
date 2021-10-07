from django.contrib import admin

from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')
    list_editable = ('parent_category',)
    prepopulated_fields = {'slug':('name',)}
    fields = (('name', 'slug'), 'short_description', 'parent_category','created_by', 'updated_by')



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    list_editable = ('price', 'is_available')
    prepopulated_fields = {'slug':('name',)}
    fields = (('name', 'slug'), 'price', 'description', 'category', 'is_available',  'created_by', 'updated_by')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductImage)

# Register your models here.
