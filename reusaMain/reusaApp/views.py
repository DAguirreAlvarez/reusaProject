from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'reusaMain.html')

def contacto(request):
    return render(request, 'contact.html')

def catalogo(request):
    return render(request, 'clothing.html')