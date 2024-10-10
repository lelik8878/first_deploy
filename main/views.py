from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
def get_home(request):
    return render(request,"home.html")

@api_view(['GET'])
def get_product_list(request):
    
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, context={'request': request})
    
    
    return Response(serializer.data)