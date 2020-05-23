import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from itertools import chain


class ListProducts(APIView):
    def get(self, request):
        _all = ProductItem.objects.all()
        ser = ProductsSerializer(_all, many=True)
        return Response(ser.data)


class ProductDetails(APIView):
    def get(self, request, pk):
        details = ProductItem.objects.get(item_id=pk)
        return Response(ProductsSerializer(instance=details).data)


class ProductSearch(APIView):
    def post(self, request):
        # body = json.loads(request.data.decode('utf-8'))
        text = request.data['search-text']

        list1 = ProductItem.objects.filter(item_desc__icontains=text)
        list2 = ProductItem.objects.filter(item_cat__cat_name__icontains=text)

        _list = chain(list1, list2)

        return Response(ProductsSerializer(_list, many=True).data)
