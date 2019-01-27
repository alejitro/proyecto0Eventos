from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


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
