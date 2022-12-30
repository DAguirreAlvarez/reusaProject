from django import forms
from django.core import validators
from .models import Product

class FormProduct(forms.ModelForm):
    sex_options = [
            ("Hombre","Hombre"),
            ("Mujer","Mujer"),
            ("Unisex","Unisex")]
    sex= forms.ChoiceField(label="Género",choices= sex_options)
    class Meta:
        model = Product
        # exclude = ()
        # fields = '__all__'
        fields= ('category', 'size','price','sex','color','brand','image')
        labels={
            'category': 'Categoria',
            'size': "Talla",
            'price': "Precio",
            'sex': "Genero",
            'color': "Color",
            'brand': "Marca",
            'image': 'Imagen'
        }
        widgets = {
            'category': forms.TextInput(
                attrs={
                    'placeholder': 'Polera, Zapatillas, Etc',
                    'class': 'campo-categoria-form'}
                ),
            'size': forms.TextInput(attrs={'placeholder': 'S, M, L, XL, Etc'}),
            'price': forms.TextInput(attrs={'placeholder': 'Ej: 9990'}),
            'color': forms.TextInput(attrs={'placeholder': 'Blanco, Negro, Etc'}),
            'brand': forms.TextInput(attrs={'placeholder': 'Puma, DC, Vans, Etc'})
        }










