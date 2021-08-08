from django.db import models


# Create your models here.
class Jewelry_type(models.Model):
    name = models.CharField(max_length=200, unique=True)
    picture = models.ImageField(unique=True)
    description = models.TextField(unique=True)

    def __str__(self):
        return f"{Jewelry_type.name}"
