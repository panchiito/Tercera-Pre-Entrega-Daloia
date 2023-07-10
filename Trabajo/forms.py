from django import forms

class FormularioCliente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class FormularioAyudante(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class FormularioProducto(forms.Form):
    nombre = forms.CharField()
    identificador = forms.IntegerField()
    descripcion = forms.CharField()