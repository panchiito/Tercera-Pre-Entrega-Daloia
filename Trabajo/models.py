from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Ayudante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    identificador = models.IntegerField()
    descripcion = models.CharField(max_length=40)