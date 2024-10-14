from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

from main.models import Product


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