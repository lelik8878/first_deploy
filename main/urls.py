from django.urls import path

from main.views import get_home, get_product_list

urlpatterns = [
    path('',get_home,name="home"),
    path('product_list/', get_product_list)
]