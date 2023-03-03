from django.db import models

class Usuario_Cliente(models.Model):
    usuario = models.CharField(max_length=25)
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    
    def __str__(self):
        return self.usuario

class Usuario_Restaurante(models.Model):
    usuario = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.usuario

class Categoriap(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    Categoria = models.ForeignKey(Categoriap, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    PEDIDOS_ESTADOS = (
        ("P", "Proceso"),
        ("E", "Entregado")
    )
    estado = models.CharField(max_length=1, choices=PEDIDOS_ESTADOS)
    nombre = models.CharField(max_length=50)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, null=True)
    codigo = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    resenia = models.CharField(max_length=1000)
    def __str__(self):
        return self.nombre