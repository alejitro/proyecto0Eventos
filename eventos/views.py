
from . import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt




# Create your views here.


def index(request):
    events=[]
    _userID=request.session.get("user",0)
    if(_userID == 0):
        sesion=False
    else:
        sesion=True
        events = models.Event.objects.filter(person__id=_userID).order_by("creation_date")

    context={"sesion":sesion, "events":events}
    return render(request,"index.html",context)


@csrf_exempt
def register(request):

    context = {}
    return render(request, "registro.html", context)

#Se define endpoint para actualizacion de datos de usuario
@csrf_exempt
def modifyEvent(request,id):
    _event=models.Event.objects.get(pk=id)
    _categories=models.Category.objects.all()
    _type= models.Type.objects.all()
    context={"event":_event, 'categories':_categories, 'types':_type}
    return render(request, "modify.html", context)

#Se define endpoint para creacion de usuario
@csrf_exempt
def createEvent(request):
    user_id=1
    context = {'user':user_id}
    return render(request, "createEvent.html", context)

@csrf_exempt
def delete(request):
    user_id=1
    context = {'user':user_id}
    return render(request, "createEvent.html", context)