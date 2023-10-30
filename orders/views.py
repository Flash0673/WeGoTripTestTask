from rest_framework import generics

from rest_framework.response import Response
from .models import Product, Order, Payment
from .serializers import ProductSerializer, OrderSerializer, PaymentSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateOrderAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        order.total_amount = sum(product.price for product in serializer.validated_data['products'])
        order.save()


class CreatePaymentAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.amount = payment.order.total_amount
        payment.save()
