from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions

from category.models import Category
from category.serializers import CategorySerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()
    lookup_field = 'id'






















