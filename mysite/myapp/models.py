from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    descriptions = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name