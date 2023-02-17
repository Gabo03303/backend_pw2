from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comentario
from .models import Categoria
from django.core import serializers
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

# /endpoints/restaurantes/listar    (pantalla 3)
def obtenerRestaurantes(request):
    if request.method == "GET":
        idCategoria = request.GET.get("categoria")

        if idCategoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)


        retaurantes = [
            {
                "id": 1,
                "nombre": "Norkys",
                "url": "https://www.deliverylima.net/wp-content/uploads/2020/07/Norkys-Logo.png",
                "estado":"A",
                "categoria": 4
            },
            {
                "id": 2,
                "nombre": "Pardos",
                "url": "https://pbs.twimg.com/profile_images/1339984045137129475/R6D7MbMF_400x400.jpg",
                "estado":"A",
                "categoria": 4
            },
            {
                "id": 3,
                "nombre": "La LeÃ±a",
                "url" : "http://4.bp.blogspot.com/-UW67YRpltq8/Ux81536Te4I/AAAAAAAAAwo/XOM6LOx2beY/s1600/la+le%C3%B1a+logo.jpg",
                "estado":"A",
                "categoria": 4
            },
            {
                "id": 4,
                "nombre": "Rosa Nautica",
                "url" : "https://scontent.flim18-2.fna.fbcdn.net/v/t1.18169-9/28279239_1605454512824084_3047163406869284348_n.png?_nc_cat=100&ccb=1-7&_nc_sid=174925&_nc_eui2=AeHY_5FHv_AcvqXToxKpuk9LE7y1ErD6MyUTvLUSsPozJWx65YaBCM95PJgB7K3LehuqPkeRnEm6gwvFqSmtP0-k&_nc_ohc=4hy3FbPEN_IAX8erPkx&_nc_ht=scontent.flim18-2.fna&oh=00_AfAgoUwjnHXVgDbe03wcN_Qn0FsbOxmDItO9lr9yx-LeWA&oe=6415C0C0",
                "estado":"A",
                "categoria": 5
            },
            {
                "id": 5,
                "nombre": "Mi Barrunto",
                "url" : "https://www.mibarrunto.com/images/logo-mi-barrunto.png",
                "estado":"A",
                "categoria": 5
            },
            {
                "id": 6,
                "nombre": "Embarcadero 41",
                "url" : "https://scontent.flim18-2.fna.fbcdn.net/v/t39.30808-6/317727454_5763745607024529_6511725448466292016_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=174925&_nc_eui2=AeFNGrV3TRDxjX2T4-i6Z60pX8TmyAl-a29fxObICX5rb1nB9VavjgZQ63plXviYl2O3m4fg_K4HsR0bGBcRuh9q&_nc_ohc=zHYOowDGmYkAX8rUKxY&_nc_ht=scontent.flim18-2.fna&oh=00_AfC9364W-MfegIKlOBqtmbxF5zXZfEk1cjPa-Ajls5plfg&oe=63F44C7F",
                "estado":"A",
                "categoria": 5
            },
            {
                "id": 7,
                "nombre": "Mc Donalds",
                "url" : "https://www.mcdonalds.com.pe/images/layout/mcdonalds-logo-bg-red.png",
                "estado":"A",
                "categoria": 1
            },
            {
                "id": 8,
                "nombre": "KFC",
                "url" : "https://i.pinimg.com/originals/ee/fd/cf/eefdcf8f23c277bfac155152c6ab3a20.jpg",
                "estado":"A",
                "categoria": 1
            },
            {
                "id": 9,
                "nombre": "Bembos",
                "url" : "https://logosenvector.com/logo/img/bembos-104.jpg",
                "estado":"A",
                "categoria": 1
            },
            {
                "id": 10,
                "nombre": "Pizza Hut",
                "url" : "https://graffica.info/wp-content/uploads/2017/07/Pizza_Hut_Logo_3.png",
                "estado":"A",
                "categoria": 2
            },
            {
                "id": 11,
                "nombre": "Papa Jhons",
                "url" : "https://www.deliverylima.net/wp-content/uploads/2020/07/Papa-Johns-Pizza-Logo.png",
                "estado":"A",
                "categoria": 2
            },
            {
                "id": 12,
                "nombre": "Mama Tomato",
                "url" : "https://www.perurunners.com/beneficios/82/202.jpg",
                "estado":"A",
                "categoria": 2
            }
        ]
        restaurantesFiltrados = []

        if idCategoria == "-1":
            restaurantesFiltrados = retaurantes
        else:
            for p in retaurantes:
                if p["categoria"] == int(idCategoria):
                    restaurantesFiltrados.append(p)

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

# pedidos/listar (Pantalla7)
def obtenerPedidos(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Categoria.objects.all()
        listaCategorias =[]
        for c in listaCategoriasQuerySet:
            listaCategorias.append({
                "id":c.id,
                "nombre":c.nombre
            })
        
        dictOk = {
            "error": "",
            "categorias": listaCategorias
        }
        return HttpResponse(json.dumps(dictOk))
    else:
        dictError = {
            "error":"Peticion inexistente"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)