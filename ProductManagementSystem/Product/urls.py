from django.contrib import admin
from django.urls import path
from .views import HomepageView,AddProductView,ListProductView


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('add', AddProductView.as_view(), name='add_product'),
    path('list-product',ListProductView.as_view(), name='product_list')

]
