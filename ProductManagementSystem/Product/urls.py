from django.contrib import admin
from django.urls import path
from .views import HomepageView,AddProductView,ListProductView,EditProductView,DeleteProductView


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('add', AddProductView.as_view(), name='add_product'),
    path('list-product',ListProductView.as_view(), name='product_list'),
    path('edit-product/<int:pk>',EditProductView.as_view(), name='edit_product'),
    path('delete-product/<int:pk>',DeleteProductView.as_view(),name='delete_product'),

]
