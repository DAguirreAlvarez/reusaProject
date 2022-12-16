from django.shortcuts import render, redirect, HttpResponse
from reusaApp.models import Product

# Create your views here.


def index(request):
    return render(request,'reusaMain.html')

def contacto(request):
    return render(request, 'contact.html')

def catalogo(request):
    return render(request, 'clothing.html')

def addProduct(request):
    return render(request, 'addProduct.html')



def agregarProducto(request):

    if request.method == 'POST':
        category = request.POST['category']
        size = request.POST['size']
        price = request.POST['price']
        sex = request.POST['sex']
        color = request.POST['color']
        brand = request.POST['brand']

        product = Product(
            category = category,
            size = size,
            price = price,
            sex = sex,
            color = color,
            brand = brand
        )

        product.save()
        return HttpResponse("<p>Producto creado:</p>")
    else:
        return HttpResponse("<p>No ha podido almacenar el producto.</p>")