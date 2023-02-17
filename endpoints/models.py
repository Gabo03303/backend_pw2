from django.db import models

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    CATEGORIA_ESTADOS = (
        ("A","Activo"),
        ("I", "Inactivo")
    )
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=1,choices=CATEGORIA_ESTADOS)
    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    PEDIDOS_ESTADOS = (
        ("P", "Proceso"),
        ("E", "Entregado")
    )
    estado = models.CharField(max_length=1, choices=PEDIDOS_ESTADOS)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    resenia = models.CharField(max_length=1000)
    def __str__(self):
        return self.nombre