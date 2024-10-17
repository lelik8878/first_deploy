from django.urls import path

from main.views import get_home, get_product_list, get_api_j, add_product, send_data

urlpatterns = [
    path('',get_home, name="home"),
    path('api/',get_product_list, name="api"),
    path('api_j/',get_api_j, name="api_j"),
    path('add_product/',add_product, name="add_product"),
    path('send_data/',send_data, name="send_data"),
]