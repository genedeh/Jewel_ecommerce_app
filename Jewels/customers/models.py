from django.db import models
from Product.models import Jewelry


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    image = models.ImageField(blank=True, default='/no_profile_image.jpg')
    password = models.CharField(max_length=8, unique=True)
    order = models.ManyToManyField('Order')
    wishlist = models.ManyToManyField("WishList")

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.CharField(max_length=180)
    order_item = models.ManyToManyField('OrderItem')

    def __str__(self):
        return f'{self.name}'


class OrderItem(models.Model):
    product = models.ForeignKey(Jewelry, on_delete=models.PROTECT)

    def __str__(self):
        return f'OrderItem Product: {self.product}'


class WishList(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    jewelry = models.ManyToManyField(Jewelry)

    def __str__(self):
        return f'{self.name}'
