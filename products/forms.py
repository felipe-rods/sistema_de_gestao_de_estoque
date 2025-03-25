from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['name', 'brand', 'category', 'description', 'serial_number', 'cost_price', 'sale_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome',
            'brand': 'Marca',
            'category': 'Categoria',
            'description': 'Descrição',
            'serial_number': 'Número de Série',
            'cost_price': 'Preço de Compra',
            'sale_price': 'Preço de Venda',
        }
