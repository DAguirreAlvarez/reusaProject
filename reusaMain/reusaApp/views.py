from django.shortcuts import render, redirect, HttpResponse
from reusaApp.models import Product
from reusaApp.forms import FormProduct, RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    return render(request,'reusaMain.html')

def contacto(request):
    return render(request, 'contact.html')

def catalogo(request):
    products = Product.objects.all()
    return render(request, 'clothing.html',{
        'productos' : products
    })

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
        return redirect("Productos")
    else:
        return HttpResponse("<p>No ha podido almacenar el producto.</p>")


def deteleProduct(request,id):
    product = Product.objects.get(pk=id)
    if product.image:
        product.image.delete()
    product.delete()
    
    return redirect("Productos")

# -------------------------------------------------------

def guardar(request):
    return render(request, "updateFrom.html")

def saveProductForm(request):
    if request.method == "POST":
        form = FormProduct(request.POST, request.FILES)
        if form.is_valid():
            data_form = form.cleaned_data

            category = data_form.get("category")
            size = data_form["size"]
            price = data_form["price"]
            sex = data_form["sex"]
            color = data_form["color"]
            brand = data_form["brand"]
            image = data_form["image"]
            # ------
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
            return redirect("Productos")
    else:
        form = FormProduct()
    return render(request, 'createFrom.html',{
        'form': form
    })

def selectProductForm(request, id):
    producto = Product.objects.get(pk=id)
    form = FormProduct(instance=producto)
    return render(request, "updateForm.html",{
        "form":form
    })

def updateProductForm(request, id):
    producto = Product.objects.get(pk=id)
    if request.method == "POST":
        form = FormProduct(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("Productos")
    else:
        form = FormProduct(instance=producto)
    return render(request, "updateForm.html",{
        "form":form
    })


def register(request):
    register_form = RegisterForm()

    if request.method=="POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("index")
    
    return render(request, "register.html",{
        "register_form": register_form
    })
