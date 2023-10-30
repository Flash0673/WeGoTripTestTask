from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('IN_PROGRESS', 'В обработке'),
        ('CONFIRMED', 'Подтвержден'),
    )

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='IN_PROGRESS')
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id}"


class Payment(models.Model):

    STATUS_CHOICES = (
        ('PAID', 'Оплачен'),
        ('IN_PROGRESS', 'В обработке'),
        ('DECLINED', 'Отменен'),
    )

    PAYMENT_TYPES = (
        ('CARD', 'Карта'),
        ('CASH', 'Наличные'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='IN_PROGRESS')
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPES, default='CARD')
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"
