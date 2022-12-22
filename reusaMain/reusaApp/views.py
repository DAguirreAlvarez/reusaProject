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

def listProduct(request):

    products = Product.objects.order_by("id")

    return render(request, 'listProducts.html',{
        'productos' : products
    })

def orderBy(request,order):
    products = Product.objects.order_by(order)

    return render(request,'listProducts.html',{
        'productos' : products
    })


def agregarProducto(request):

    if request.method == 'POST':
        category = request.POST['category']
        size = request.POST['size']
        price = request.POST['price']
        sex = request.POST['sex']
        color = request.POST['color']
        brand = request.POST['brand']
        image = request.FILES['image']

        product = Product(
            category = category,
            size = size,
            price = price,
            sex = sex,
            color = color,
            brand = brand,
            image = image
        )

        product.save()
        return HttpResponse("<p>Producto creado:</p>")
    else:
        return HttpResponse("<p>No ha podido almacenar el producto.</p>")

def selectProduct(request,id):

    product = Product.objects.get(pk=id)
    return render(request, 'updateProduct.html',{
        'producto' : product
    })

def updateProduct(request, id):
    if request.method == 'POST':
        id = id
        category = request.POST['category']
        size = request.POST['size']
        price = request.POST['price']
        sex = request.POST['sex']
        color = request.POST['color']
        brand = request.POST['brand']

        product = Product(
            pk = id,
            category = category,
            size = size,
            price = price,
            sex = sex,
            color = color,
            brand = brand,
        )
        product.save()
    return redirect("Productos")

def deteleProduct(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    
    return redirect("Productos")

