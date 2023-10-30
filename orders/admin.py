import time
import datetime
import requests
from django.contrib import admin
from .models import Product, Order, Payment

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.shortcuts import get_object_or_404
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_amount', 'status', 'created_at', 'confirmed_at']

    actions = ['confirm_order']

    def confirm_order(self, request, queryset):
        for order in queryset:
            if order.payment_set.filter(status='PAID').exists():
                # Подготовка заказа
                time.sleep(5)

                payload = {
                    'id': order.id,
                    'amount': float(order.total_amount),
                    'date': str(order.confirmed_at)
                }
                response = requests.post('https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4', json=payload)

                order.status = 'CONFIRMED'
                order.confirmed_at = datetime.now()
                order.save()

                return JsonResponse(response.json(), safe=False)

    confirm_order.short_description = 'Подтвердить выбранные заказы'


admin.site.register(Product)
admin.site.register(Payment)
