from django import forms

from main.models import Product, ProductProperties


class ProductForm(forms.Form):
    CHOICES = [('кг', 'кг'), ('л', 'л'), ('г', 'г'), ('шт', 'шт')]
    product_title = forms.CharField(label='Название продукта')
    product_image = forms.ImageField(label='Изображение продукта')
    product_price = forms.IntegerField(label='Цена')
    product_unit = forms.ChoiceField(label='Единица измерения', choices=CHOICES)


class ProductPropertiesForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Продукт')
    weight = forms.DecimalField(label='Вес')
