from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import productSerializer
from .models import Product


# Create your views here.
"""@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/product-list/',
        'Detail View':'/product-detail/<int:id>',
        'Create':'/product-create/',
        'Update':'/product-update/<int:id>',
        'Delete':'/product-detail/<int:id>',


    }
    return Response(api_urls);
"""
@api_view(['GET'])
def ShowAll(request):
    products=Product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request,pk):
    product=Product.objects.get(id=pk)
    serializer=productSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = productSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request, pk):
    product=Product.objects.get(id=pk)
    serializer = productSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteProduct(request, pk):
    product=Product.objects.get(id=pk)
    # serializer = productSerializer(instance=product,data=request.data)
    product.delete()
    return Response('Items delete successfully')

