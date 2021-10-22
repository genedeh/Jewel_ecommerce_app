from django.db import models


# Create your models here.
class Jewelry_type(models.Model):
    name = models.CharField(max_length=200, unique=True)
    picture = models.ImageField(default='/No product image.png')
    description = models.TextField(unique=True)

    def __str__(self):
        return f"{self.name}"


class Jewelry(models.Model):
    name = models.CharField(max_length=250, unique=True)
    jewelry_type = models.ForeignKey(Jewelry_type, on_delete=models.PROTECT, default=1)
    image = models.ImageField(default='/No product image.png')
    video = models.FileField(blank=True)
    description = models.TextField()
    stock_count = models.IntegerField()
    slug = models.SlugField(default=name.name)
    price = models.FloatField(help_text='Currency in naira')
    star = models.FloatField()

    def __str__(self):
        return f'{self.name}'