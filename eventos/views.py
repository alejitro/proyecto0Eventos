from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import models
from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.


def index(request):
    #return HttpResponse("Eventos Up")
    sesion=False
    context={"sesion":sesion}
    return render(request,"index.html",context)

@csrf_exempt
def registro(request):
    #email=request.post().get('email')
    #password=request.post().get('password')
    context = {}
    return render(request, "registro.html", context)
