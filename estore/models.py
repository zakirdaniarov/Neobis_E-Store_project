from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORY_PRODUCT = (
        ('digital services', 'digital services'),
        ('cosmetics and body care', 'cosmetics and body care'),
        ('food and beverage', 'food and beverage'),
        ('health and wellness', 'health and wellness'),
        ('household items', 'household items'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=150, choices=CATEGORY_PRODUCT)

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'
# Create your models here.
