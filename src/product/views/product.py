from json import loads
from typing import Dict
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from django.http import JsonResponse
from django.views.generic import View

from product.models import Product
from product.serializers import ProductSerializer
from category.models import Category


class ProductListCreateAPIView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()
    lookup_field = 'id'


class ProductView(View):

    def post(self, request):
        import pdb;
        pdb.set_trace()
        body: str = request.body.decode('utf-8')
        req_body: Dict = loads(body)
        product = Product()
        product.name = req_body['name']
        product.price = req_body['price']
        product.description = req_body['description']
        product.category = Category.objects.get(pk=req_body['category'])
        product.save()

        data = product_serializer(product)
        return JsonResponse(data=data, status=201)

    def get(self, request):
        product = Product.objects.all()
        data = product_serializer(product)
        return JsonResponse(data=data, status=200, safe=False)



