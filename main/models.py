from django.db import models

class Product(models.Model):
    CHOICES = [('кг', 'кг'), ('л', 'л'), ('г', 'г'), ('шт', 'шт')]
    title = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.IntegerField()
    unit = models.CharField(max_length=255, choices=CHOICES)


class ProductProperties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)