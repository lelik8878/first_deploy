from django.urls import path

from main.views import get_home, get_product_list, get_api_j, get_add_product_page, send_data

urlpatterns = [
    path('',get_home, name="home"),
    path('api/',get_product_list ,name="api"),
    path('api_j/',get_api_j ,name="api_j"),
    path('add_product/', get_add_product_page, name='add_product'),
    path('send_data/',send_data ,name="send_data"),
]