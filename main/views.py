import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import ProductForm, ProductPropertiesForm
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
    api_j = {'name': 'Johan', 'age': 23}
    return JsonResponse(api_j)

def add_product(request):
    products = Product.objects.all()
    product_form = ProductForm()
    product_properties_form = ProductPropertiesForm()
    print(request.POST)
    if request.method == 'POST':
        new_product = ProductForm(request.POST, request.FILES)
        new_product_properties = ProductPropertiesForm(request.POST)
        if new_product.is_valid():
            pre_save_product = Product(title=new_product.cleaned_data.get('product_title'),
                                       image=new_product.cleaned_data.get('product_image'),
                                       price=new_product.cleaned_data.get('product_price'),
                                       unit=new_product.cleaned_data.get('product_unit'))
            pre_save_product.save()
        if new_product_properties.is_valid():
            pre_save_product_properties = ProductProperties(product=new_product_properties.cleaned_data.get('product'),
                                                            weight=new_product_properties.cleaned_data.get('weight'))
            pre_save_product_properties.save()
    context = {'products': products,
               'product_form': product_form,
               'product_properties_form': product_properties_form}
    return render(request,"add_product.html", context)


def send_data(request):
    print(request.body)
    new_data = json.loads(request.body)
    print(new_data)
    print(type(new_data))
    return JsonResponse({})
