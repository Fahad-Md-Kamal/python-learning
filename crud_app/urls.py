from typing import Pattern
from django.urls import path
from . import views


app_name = 'crud'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='home-page' ),
    path('add-category', views.category_create_view, name='add_category' ),
]