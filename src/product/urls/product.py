from django.urls import path
from product.views import ProductView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='product_create_view'),
    path('<int:id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='update view')

]
