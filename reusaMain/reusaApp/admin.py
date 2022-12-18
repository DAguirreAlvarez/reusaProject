from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['pk']

# Agregamos el CRUD a la pagina del administrador
admin.site.register(Product, ProductAdmin)