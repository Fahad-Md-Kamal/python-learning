from typing import Pattern
from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.homepage_view, name='home-page' ),
    path('add-category', views.category_create_view, name='add_category' ),
    path('update-category/<slug:slug>', views.category_update_view, name='update_category' ),
    path('add-product/', views.add_product_view, name='add_product' ),
    path('update-product/<slug:slug>', views.update_product_view, name='update_product' ),
    path('detail-product/<slug:slug>', views.detail_product_view, name='product_detail' ),
]