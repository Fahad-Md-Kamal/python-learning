from django.urls import path
from products.views import chart_select_view

app_name = 'products'

urlpatterns = [
    path('', chart_select_view, name='product-list'),
]