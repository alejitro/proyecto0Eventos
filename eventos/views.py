
from . import models
from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.


def index(request):
    #return HttpResponse("Eventos Up")
    sesion=False
    context={"sesion":sesion}
    return render(request,"index.html",context)


def registro(request):

    context = {}
    return render(request, "registro.html", context)
