from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_image/')
    price = models.IntegerField()
    
    
    def __str__(self):
        return self.title
    
class Quantity(models.Model):
    CHOICES = [('кг','кг'), ('л','л'), ('г','г'), ('шт','шт')]
    
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=255, choices=CHOICES)