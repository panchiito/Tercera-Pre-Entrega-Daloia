from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from Trabajo.forms import *
from Trabajo.models import *

# Create your views here.

def index(request):
    return render(request, "Trabajo/index.html")

def hija(request):
    return render(request, "Trabajo/hija.html")


def clientes(request):
    if request.method == "POST":
        miFormulario = FormularioCliente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            cliente.save()
            return render(request, "Trabajo/index.html")
    else:
        miFormulario = FormularioCliente()
    return render(request, "Trabajo/clientes.html", {"miFormulario":miFormulario})



def ayudantes(request):
    if request.method == "POST":
        miFormulario = FormularioAyudante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            ayudante = Ayudante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            ayudante.save()
            return render(request, "Trabajo/index.html")
    else:
        miFormulario = FormularioAyudante()
    return render(request, "Trabajo/ayudantes.html", {"miFormulario":miFormulario})



def productos(request):
    if request.method == "POST":
        miFormulario = FormularioProducto(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(nombre=informacion["nombre"], identificador=informacion["identificador"], descripcion=informacion["descripcion"])
            producto.save()
            return render(request, "Trabajo/index.html")
    else:
        miFormulario = FormularioProducto()
    return render(request, "Trabajo/productos.html", {"miFormulario":miFormulario})


def busquedaCliente(request):
    return render(request, "Trabajo/busquedaCliente.html")

def busquedaAyudante(request):
    return render(request, "Trabajo/busquedaAyudante.html")

def buscar(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        nombre = Cliente.objects.filter(apellido__icontains=apellido)
        return render(request, "Trabajo/resultadosPorBusqueda.html", {"nombres": nombre, "apellido":apellido})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def buscarAyudante(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        nombre = Ayudante.objects.filter(apellido__icontains=apellido)
        return render(request, "Trabajo/resultadosPorBusqueda.html", {"nombres": nombre, "apellido":apellido})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def padre(request):
    return render(request, "Trabajo/padre.html")

def components(request):
    return render(request, "Trabajo/components.html")



