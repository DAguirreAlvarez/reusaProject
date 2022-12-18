from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Product(models.Model):
    category = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    sex =  models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    brand = models.CharField(max_length=30)
    image = models.ImageField(default='null', upload_to="products")
    
    class Meta:
        # verbose_name es para cuando se muestra la lista desplegada de registros de esta tabla.
        verbose_name = "Product"
        # verbose_name_plural es para cuando nos muestra las tablas que tenemos en la db.
        verbose_name_plural = "Products"
        # Ordenamos en base al id de manera descendente, esto es debido al simbolo -
        # Este orden es solo para el panel de administracion de Django.
        ordering = ['-id']

    def __str__(self):
        return f"{self.pk} - {self.category} - {self.color} - {self.brand}"