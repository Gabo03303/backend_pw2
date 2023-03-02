from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Plato)
admin.site.register(models.Categoria)
admin.site.register(models.Pedidos)
admin.site.register(models.Comentario)
admin.site.register(models.Restaurante)
admin.site.register(models.Categoriap)
admin.site.register(models.Usuario_Cliente)
admin.site.register(models.Usuario_Restaurante)