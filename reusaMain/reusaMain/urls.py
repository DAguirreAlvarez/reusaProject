"""reusaMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reusaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', views.index, name='index'),
    path('', views.index, name="Inicio"),
    path('contacto', views.contacto, name="Contacto"),
    path('catalogo', views.catalogo, name="Catalogo"),
    path('productos',views.listProduct, name="Productos"),
    path('agregarp', views.addProduct, name="AgregarProducto"),
    path('guardar-producto', views.agregarProducto, name="btnGuardarProducto"),
    path('productos/<str:order>', views.orderBy, name="Ordernar"),
    path('borrarProduct/<int:id>', views.deteleProduct, name="Eliminar"),
    path('seleccionarProduct/<int:id>', views.selectProduct, name="Seleccionar"),
    path('actualizarProduct/<int:id>', views.updateProduct, name="Actualizar"),
]
