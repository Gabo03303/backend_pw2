from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comentario, Restaurante, Categoria, Categoriap, Plato, Pedidos, Usuario_Cliente, Usuario_Restaurante

import json


# /endpoints/loginCliente    (pantalla 1)
@csrf_exempt
def loginCliente(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        usuarios = Usuario_Cliente.objects.all()

        for u in usuarios: 
            if u.usuario == usuario and u.password == password:
                dictOK = {
                    'error': '',
                    'userid': u.pk
                }
                return HttpResponse(json.dumps(dictOK))
            else:
                dictError = {
                'error': 'No existe esa cuenta'
                }
                strError = json.dumps(dictError)
                return HttpResponse(strError)
    else:
        dictError = {
            'error': 'Tipo de peticion no existe'
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    
# /endpoints/loginRestaurante    (pantalla 9)
@csrf_exempt
def loginRestaurante(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        usuarios = Usuario_Restaurante.objects.all()

        for u in usuarios: 
            if u.usuario == usuario and u.password == password:
                dictOK = {
                    'error': '',
                    'userid': u.pk
                }
                return HttpResponse(json.dumps(dictOK))
            else:
                dictError = {
                'error': 'No existe esa cuenta'
                }
                strError = json.dumps(dictError)
                return HttpResponse(strError)
    else:
        dictError = {
            'error': 'Tipo de peticion no existe'
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)



# /endpoints/categorias/listar (Pantalla3)
def obtenerCategorias(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Categoria.objects.all()
        listaCategorias = []
        for c in listaCategoriasQuerySet:
            listaCategorias.append({
                "id" : c.id,
                "nombre" : c.nombre
            })

        dictOK = {
            "error" : "",
            "categorias" : listaCategorias
        }
        return HttpResponse(json.dumps(dictOK))

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
# /endpoints/restaurantes/listar    (pantalla 3)

def obtenerRestaurantes(request):
    if request.method == "GET":
        idCategoria = request.GET.get("categorias")
        print(idCategoria)
        if idCategoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        restaurantesFiltrados = []

        if idCategoria == "-1":
            restaurantesQS = Restaurante.objects.all()
        else:
            restaurantesQS =    Restaurante.objects.filter(categoria__pk = idCategoria)
        print(restaurantesQS)
        for p in restaurantesQS:
            
                restaurantesFiltrados.append({
                    "id":p.id,
                    "nombre":p.nombre,
                    "url":p.url,
                    "categoria" : {
                        "id":p.categoria.pk,
                        "nombre":p.categoria.nombre
                    }
                })

        dictResponse = {
            "error" : "",
            "restaurantes" : list(restaurantesFiltrados)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error" : "Error al recibir los platos"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


# /endpoints/comentarios/listar    (pantalla sorpresa)
def obtenerComentario(request):
    if request.method == "GET":
        listaComentariosQuerySet = Comentario.objects.all()
        listaComentarios = []
        for c in listaComentariosQuerySet:
            listaComentarios.append({
                "id" : c.id,
                "nombre" : c.nombre,
                "correo" : c.correo,
                "resenia" : c.resenia
            })

        dictOK = {
            "error" : "",
            "comentarios" : listaComentarios
        }
        return HttpResponse(json.dumps(dictOK))

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

# pedidos/listar (Pantalla13)
def obtenerPedidos(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Pedidos.objects.all()
        listaPedidos =[]
        for c in listaCategoriasQuerySet:
            listaPedidos.append({
                "id":c.id,
                "nombre":c.nombre,
                "estado" :c.estado,
                "codigo" :c.codigo,
                "plato" : {
                    "id": c.plato.pk,
                    "nombre" : c.plato.nombre,
                    "url" : c.plato.url
                }
            }) 
        dictOk = {
            "error": "",
            "pedidos": listaPedidos
        }
        return HttpResponse(json.dumps(dictOk))
    else:
        dictError = {
            "error":"Peticion inexistente"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

# categoriasp/listar (pantalla10) 
def obtenerCategoriasP(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Categoriap.objects.all()
        listaCategorias = []
        for c in listaCategoriasQuerySet:
            listaCategorias.append({
                "id":c.id,
                "nombre":c.nombre
            })
        dictOk = {
            "error":"",
            "categorias" : listaCategorias
        }
        return HttpResponse(json.dumps(dictOk))
    else:
        dictError = {
            "error": "Peticion Inexistente"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


#(pantalla 4)
def obtenerPlatos(request):
    if request.method == "GET":
        idCategoria = request.GET.get("categorias")
        if idCategoria == None:
            dictError = {
                "error": "Debe enviar una categorias como query parameter"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        
        platosFiltrados = []

        if idCategoria == "-1":
            platosQS = Plato.objects.all()
        else:
            platosQS = Plato.objects.filter(Categoria__pk = idCategoria)
        for p in platosQS:
            platosFiltrados.append({
                "id": p.id,
                "nombre": p.nombre,
                "url": p.url,
                "categoria" : {
                    "id": p.Categoria.pk,
                    "nombre" : p.Categoria.nombre
                }
            })
        
        dictResponse = {
            "error" : "",

            "platos" : list(platosFiltrados)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    
    else:
        dictError = {
            "error" : "Error al recibir los platos"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    

    
