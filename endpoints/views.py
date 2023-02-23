from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comentario, Restaurante, Categoria, Categoriap, Plato, Pedidos

import json

#/endpoints/platos/listar (Pantalla10)
def obtenerPlatos(request):
    if request.method == "GET":
        categoria = request.GET.get("categoria")
        if categoria == None:
            dictError = {
            "error" : "Debe enviar una categoria como query parameter"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        platos = [
            {
            "id": 1,
            "nombre": "Conchitas a la Parmesana",
            "precio": "20",
            "url": " https://1.bp.blogspot.com/-1gpQXGuUxZY/X-NR-IfTK5I/AAAAAAAAPKk/GPFcQrTeYRQSUctlJjcvOajaoLuElqMSgCLcBGAsYHQ/s1200/Conchitas%2Ba%2Bla%2Bparmesana.jpg",
            "categoria": 1
        },
            {
            "id": 1,
            "nombre": "Causa de Pollo",
            "precio": "25",
            "url": "https://elcomercio.pe/resizer/1xz3w_26FwRA5JuSn02p9afc97g=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/7QDRJTB2DZHB7IQL3HF4IK6OX4.jpg",
            "categoria": 1
        },
            {
            "id": 1,
            "nombre": "Leche de Tigre",
            "precio": "15",
            "url": "https://elcomercio.pe/resizer/6TR0Lcwmg4Z_vm0JlNbscb4JNMA=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/VN5X2O53B5E4VINDN7TGWQLUQ4.jpg",
            "categoria": 1
        },
            {
            "id": 2,
            "nombre": "Ceviche de Pesacdo",
            "precio": "30",
            "url": "https://trome.pe/resizer/-R8GQPfZoAOK4V9uCalvv6FeYEs=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/KMEMVCZ2KJAATPYX2JT7FDPT5Q.jpg",
            "categoria": 2
        },
            {
            "id": 2,
            "nombre": "Jalea Mixta",
            "precio": "35",
            "url": "https://www.comedera.com/wp-content/uploads/2022/06/jalea-mixta.jpg",
            "categoria": 2
        },
            {
            "id": 2,
            "nombre": "Arroz con Mariscos",
            "precio": "35",
            "url": "https://elcomercio.pe/resizer/2NsfDVlLCtb6UlSre99ZthqWhP8=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/NEE6QF2DE5D7VIM3CTX3SBU6FI.jpg",
            "categoria": 2
        },
            {
            "id": 3,
            "nombre": "Chicha Morada",
            "precio": "20",
            "url": "https://elcomercio.pe/resizer/hFBXMzUVwnOLwhZrKRyKUOYx_dU=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/UZW3LRBMABAA5IZPHJ36MJZX5I.jpg",
            "categoria": 3
        },
            {
            "id": 3,
            "nombre": "Limonada ",
            "precio": "15",
            "url": "https://cloudfront-us-east-1.images.arcpublishing.com/infobae/CLWWVAIRGJF4FG4ATXCV7YZZLQ.jpg",
            "categoria": 3
        },
            {
            "id": 3,
            "nombre": "Maracucya",
            "precio": "18",
            "url": "https://peru21.pe/resizer/-DolEImJY18leOPdibu4kyKIjb8=/1200x800/smart/filters:format(jpeg):quality(75)/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/G5XOTKDEENAX7JYZMWI4YYGD24.jpg",
            "categoria": 3
        },
            {
            "id": 4,
            "nombre": "Torta de Chocolate",
            "precio": "10",
            "url": "https://peru21.pe/resizer/YmGwSw9bXc2Hgoua1WgdNhw2hN0=/1200x800/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/EJLK47B5TRBDFPD4FMZXUWCWZQ.png",
            "categoria": 4
        },
            {
            "id": 4,
            "nombre": "Flan",
            "precio": "12",
            "url": "https://www.recetasnestle.com.mx/sites/default/files/srh_recipes/0c7289c004b75116015878c651519e10.jpg",
            "categoria": 4
        },
            {
            "id": 4,
            "nombre": "Mousse de Mango",
            "precio": "14",
            "url": "https://sivarious.com/wp-content/uploads/2022/05/mousse-de-mango.jpg",
            "categoria": 4
        },
            {
            "id": 5,
            "nombre": "Helado de Fresa",
            "precio": "10",
            "url": "https://www.comedera.com/wp-content/uploads/2022/04/Helado-de-fresas-casero-shutterstock_1477385882.jpg",
            "categoria": 5
        },
            {
            "id": 5,
            "nombre": "Helado de Menta",
            "precio": "10",
            "url": "https://t1.uc.ltmcdn.com/es/posts/4/6/9/como_hacer_helado_de_menta_28964_orig.jpg",
            "categoria": 5
        },
            {
            "id": 5,
            "nombre": "Helado de Vainilla",
            "precio": "8",
            "url": "https://i.pinimg.com/originals/fe/2e/ff/fe2eff0b461f9043018b0f995412805d.jpg",
            "categoria": 5
        }
        ]
        platosFiltrados = []
        if categoria == "-1":
            platosFiltrados = platos
        else:
            for p in platos:
                if p["categoria"] == int(categoria):
                    platosFiltrados.append(p)

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

# /endpoints/loginCliente    (pantalla 1)
@csrf_exempt
def loginCliente(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        correo = dictDataRequest["correo"]
        password = dictDataRequest["password"]

        # TODO: Consultar a base de datos
        if correo == "pw@aloe.ulima.edu.pe" and password == "ulima":
            # Correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
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

        # TODO: Consultar a base de datos
        if usuario == "restaurante" and password == "restaurante":
            # Correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

# /endpoints/Login8
@csrf_exempt
def login8(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        # TODO: Consultor a base de datos
        if usuario == "74229263" and password == "ABC-123":
            # correcto
            dictOk = {
                "error": ""
            }
            return HttpResponse(json.dumps(dictOk))
        else:
            # Error Login
            dictError = {
                "error": "Error en login"
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
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
            if p["categoria"] == int(idCategoria):
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
                "id":c.pk,
                "nombre":c.nombre,
                "estado" :c.estado,
                "codigo" :c.codigo,
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
def obtenerPeliculas(request):
    if request.method == "GET":
        idCategoria = request.GET.get("categoria")


        if idCategoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)


        peliculasFiltradas = []


        if idCategoria == "-1" :
            peliculasQS = Plato.objects.all()
        else:
            peliculasQS = Plato.objects.filter(categoria__pk=idCategoria)

        for p in peliculasQS:
            peliculasFiltradas.append({
                "id" : p.pk,
                "nombre" : p.nombre,
                "url" : p.url,
                "categoria" : {
                    "id" : p.Categoria.pk,
                    "nombre" : p.Categoria.nombre
                }
            })


        dictResponse = {
            "error": "",
            "peliculas": peliculasFiltradas
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


# (pantalla 4)
def obtenerCategorias4(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Categoriap.objects.all()
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