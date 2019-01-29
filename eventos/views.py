
from . import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import json
from django.views.decorators.csrf import csrf_exempt




# Create your views here.


def index(request):
    #email= request.data.get('email', None)
    #password = request.data.get('password', None)
    #user = authenticate(request, username=email, password=password)

    """
    if user is not None:
        login(request, user)
        content = {
            'msg': "Login Correcto",
            "user": {
                "email": user.email
            }
        }
        #return responses.MyResponse(responses.RESPONSE_STATUS_OK, content).res

    else:
        content = {'msg': 'El nombre de usuairo o contraseña con coinciden'}
        #return responses.MyResponse(responses.RESPONSE_STATUS_ERROR, content,
        #                            responses.HTTPStatus.HTTP_401_UNAUTHORIZED).res
    #return HttpResponse("Eventos Up")
    """
    events = models.Event.objects.all()
    sesion=True
    context={"sesion":sesion, "events":events}
    return render(request,"index.html",context)



def register(request):

    context = {}
    return render(request, "registro.html", context)

#Se define endpoint para actualizacion de datos de usuario
@csrf_exempt
def modifyEvent(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        name = data["name"]
        category = data["category"]
        place = data[place]
        address = data["address"]
        start_date = data["start_date"]
        finish_date = data["finish_date"]
        type = data["type"]
        _eventId=data["id"]

        _event=models.Event()
        if(_event.update(name, category, place,address, start_date,finish_date,type)):
            res={"status":"Ok","Content:":"Evento Modificado"}
        else:
            res={"status":"Error","Content:":"Error al modificar evento"}

        return HttpResponse(json.dumps(res),content_type="application/json")
    else:
        return  HttpResponse('Metodo no definido')

#Se define endpoint para creacion de usuario
@csrf_exempt
def createEvent(request):

        if request.method == 'POST':
            data=json.loads(request.body)
            name = data["name"]
            lastName = data["lastName"]
            email = data["email"]
            country = data["country"]
            city = data["city"]
            pws = data["password"]
            id = data["idUser"]
            _user = User(name = name,lastName=lastName,email=email,country=country,city=city,password=pws,idUser=id)
            try:
                _user.save()
                res = {"status": "Ok", "Content:": "Usuario creado"}
            except:

                res = {"status": "Error", "Content:": "Error al crear usuario"}

            return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse('Metodo no definido')