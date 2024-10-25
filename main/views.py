import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import AddProductForms
from .serializers import ProductSerializer

from main.models import Product, ProductProperties


# Create your views here.
def get_home(request):
    return render(request,"home.html")

@api_view(['GET'])
def get_product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={'request': request})

    return Response(serializer.data)

def get_api_j(request):
    api_j = {'name': 'Johan', 'age': '20'}
    return JsonResponse(api_j)

def get_add_product_page(request):
    product_properties = ProductProperties.objects.all()
    products = Product.objects.all()
    form = AddProductForms()
    if request.method == 'POST':
        form = AddProductForms(request.POST, request.FILES)
        if form.is_valid():
            new_product = Product(**form.cleaned_data)
            new_product.save()
            return redirect('home')
        else:
            print(form.errors)


    context = {
        'product_properties': product_properties,
        'products': products,
        'form': form,
    }

    return render(request, "add_product.html", context)

def send_data(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        new_product = Product()
        new_product.save()
        return  JsonResponse({})
    return JsonResponse({})