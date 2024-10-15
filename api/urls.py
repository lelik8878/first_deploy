from django.urls import path

from api.views import get_text, get_main_page, accept_data

urlpatterns = [
    path('',get_text, name="get_text"),
    path('main/',get_main_page, name="get_main"),
    path('data/',accept_data, name="accept_data"),
]