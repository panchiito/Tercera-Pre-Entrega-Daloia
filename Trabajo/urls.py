from django.urls import path
from Trabajo import views

urlpatterns = [

    path("", views.index, name="index"), 
    path("hija", views.hija, name="hija"), 
    # path("formulario1", views.formulario1, name="Formulario1"), 
    path("padre", views.padre, name="Padre"), 
    path("components", views.components, name="Componentes"), 
    path("clientes", views.clientes, name="Clientes"), 
    path("productos", views.productos, name="Productos"),
    path("ayudantes", views.ayudantes, name="Ayudantes"), 
    path("busquedaCliente", views.busquedaCliente, name="BusquedaCliente"), 
    path("busquedaAyudante", views.busquedaAyudante, name="BusquedaAyudante"), 
    path("buscar/", views.buscar), 
    path("buscarAyudante/", views.buscarAyudante), 

]