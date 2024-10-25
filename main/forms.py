from django import forms

from main.models import Product


class AddProductForms(forms.Form):
    title = forms.CharField(max_length=255, label='Название продукта',)
    image = forms.ImageField(required=False, label='Фото продукта', )
    price = forms.DecimalField(max_digits=6, decimal_places=2, label='Цена',)
    unit = forms.ChoiceField(label='Едницы измерения', choices=[('кг', 'кг'), ('л', 'л'), ('г', 'г'), ('шт', 'шт')])

class AddProductPropertiesForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Продукт',)
    weight = forms.DecimalField(label='Вес')

