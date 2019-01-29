from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import *


@csrf_exempt
def registrar(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=User.objects.create_user(email,email,password)
            user.save()
            return HttpResponse("Exito")

        except:
            return HttpResponse("Error al crear usuario")

    return HttpResponse("Metodo no valido")

@csrf_exempt
def eliminar(request):
    if(request.method=="GET"):
        try:
            ev=Event.objets.get(pk=request.GET.get("id"))
            ev.remove()
            return redirect('index')
            #return HttpResponse("Exito")

        except:
            return HttpResponse("Error al eliminar evento")

    return HttpResponse("Metodo no valido")


