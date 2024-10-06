from django.urls import path

from main.views import get_home

urlpatterns = [
    path('',get_home,name="home")
]