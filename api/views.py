from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def get_main_page(request):
    return render(request, 'main.html')

def get_text(request):
    return HttpResponse("Hello World")

def accept_data(request):
    return HttpResponse("Recieved")


