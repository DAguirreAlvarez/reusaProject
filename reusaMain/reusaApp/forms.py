from django import forms
from django.core import validators
from .models import Product

class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()
        fields = '__all__'
        
        category = forms.CharField(
            label="Categoría",
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Polera, Zapatillas, Etc',
                    'class': 'campo-categoria-form'}
                )
        )
        size = forms.CharField(
            label="Talla",
            widget=forms.TextInput(attrs={'placeholder': 'S, M, L, XL, Etc'})
        )
        price = forms.IntegerField(
            label="Precio",
            widget=forms.TextInput(attrs={'placeholder': 'Ej: 9990'}),
            validators=[
                validators.MinValueValidator(1,"Ingresa un precio superior a 0")
            ]
        )
        # Opciones de select, primero valor a almacenar y luego valor a mostrar en formulario
        sex_options = [
            ("Hombre","Hombre"),
            ("Mujer","Mujer"),
            ("Unisex","Unisex")
        ]
        sex = forms.ChoiceField(
            label="Género",
            choices = sex_options
        )


        color = forms.CharField(
            label="Color",
            widget=forms.TextInput(attrs={'placeholder': 'Blanco, Negro, Etc'})
        )
        brand = forms.CharField(
            label="Marca",
            widget=forms.TextInput(attrs={'placeholder': 'Puma, DC, Vans, Etc'})
        )

        image = forms.ImageField(
            label="Imagen"
        )





