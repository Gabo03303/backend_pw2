from django.urls import path
from . import views

urlpatterns = [
    path("loginC", views.loginCliente),
    path("loginR", views.loginRestaurante),
    path("platos/listar",views.obtenerPlatos),
    path("restaurantes/listar", views.obtenerRestaurantes),
    path("comentarios/listar", views.obtenerComentario),
    path("pedidos/listar",views.obtenerPedidos),
    path("categoriasp/listar",views.obtenerCategoriasP),
    path("categorias/listar",views.obtenerCategorias),
]