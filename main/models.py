from django.db import models

class Product(models.Model):
    CHOICES = [('кг', 'кг'), ('л', 'л'), ('г', 'г'), ('шт', 'шт')]
    title = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.IntegerField()
    unit = models.CharField(max_length=255, choices=CHOICES)

    def __str__(self):
        return self.title


class ProductProperties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='')
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='')

    def __str__(self):
        return self.product

    def __str__(self):
        return f'{self.product} --- {self.weight}'
    class Meta:
        verbose_name = 'Свойство продукта'