from django.db import models

class Product(models.Model):
    CHOICES = [('кг', 'кг'), ('л', 'л'), ('г', 'г'), ('шт', 'шт')]
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    unit = models.CharField(max_length=255, choices=CHOICES, verbose_name='Единица измерения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductProperties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='')
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='')

    def __str__(self):
        return f'{self.product} --- {self.weight}'

    class Meta:
        verbose_name = 'Свойства продукта'
        verbose_name_plural = 'Свойства продуктов'

