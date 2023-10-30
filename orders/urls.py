from django.urls import path
from .views import ProductListAPIView, CreateOrderAPIView, CreatePaymentAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('create_order/', CreateOrderAPIView.as_view(), name='create-order'),
    path('create_payment/', CreatePaymentAPIView.as_view(), name='create-payment'),
]
