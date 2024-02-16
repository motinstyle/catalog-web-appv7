from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_index),
    path('inventory', views.inventory_index)
]
