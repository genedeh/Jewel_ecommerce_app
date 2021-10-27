from django.db import models


# Create your models here.
from django.urls import reverse


class Jewelry_type(models.Model):
    name = models.CharField(max_length=200, unique=True)
    picture = models.ImageField(default='/No product image.png')
    description = models.TextField(unique=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('Product:jewelry_detail', kwargs={'pk': self.pk})


class Jewelry(models.Model):
    name = models.CharField(max_length=250, unique=True)
    jewelry_type = models.ForeignKey(Jewelry_type, on_delete=models.PROTECT, default=1, related_name='jewelries')
    image = models.ImageField(default='/No product image.png')
    video = models.FileField(blank=True)
    description = models.TextField()
    stock_count = models.IntegerField()
    slug = models.SlugField(default=name.name)
    price = models.FloatField(help_text='Currency in naira')
    star = models.SmallIntegerField()

    def __str__(self):
        return f'{self.name}'
