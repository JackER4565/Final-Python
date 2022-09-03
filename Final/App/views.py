from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.models import Crear_cuenta
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):

    dicctionary = {}
    plantilla = loader.get_template("MainPage/index_hijo.html")

    documento = plantilla.render(dicctionary)

    return HttpResponse(documento)

def crear_cuenta(request):

    dicctionary = {}
    plantilla = loader.get_template("MainPage/crear_cuenta.html")

    documento = plantilla.render(dicctionary)
    if request.method == 'POST': 
            username = request.POST.get('username', False)
            if Crear_cuenta.objects.filter(username=username).exists():
                respuesta = {"mensaje" : "Ya existe usuario."}
                return render(request,'MainPage/crear_cuenta.html',respuesta)
            
            password = request.POST.get('password', False)
            encrypted = make_password(password)
            mail = request.POST.get('mail', False)
            if Crear_cuenta.objects.filter(mail=mail).exists():
                respuesta = {"mensaje" : "Ya existe correo."}
                return render(request,'MainPage/crear_cuenta.html',respuesta)
            createacc = Crear_cuenta (username = username, password = encrypted, mail = mail)
            createacc.save()
            respuesta = {"mensaje" : "Cuenta creada correctamente."}
            return render(request,'MainPage/crear_cuenta.html',respuesta)
    return render(request,'MainPage/crear_cuenta.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        encryptedpassword=make_password(request.POST['password'])
        print(encryptedpassword)
        checkpassword=check_password(request.POST['password'], encryptedpassword)
        print(decryptedpassword)
        data=Login(email=email, password=encryptedpassword)

        data.save()
        return HttpResponse('Done')
    else:
        return render(request, 'index.html')
def actuales(request):

    dicctionary = {}
    plantilla = loader.get_template("MainPage/crear_cuenta.html")

    documento = plantilla.render(dicctionary)

    return HttpResponse(documento)

def vencidas(request):

    dicctionary = {}
    plantilla = loader.get_template("MainPage/crear_cuenta.html")

    documento = plantilla.render(dicctionary)

    return HttpResponse(documento)

def ganadores(request):

    dicctionary = {}
    plantilla = loader.get_template("MainPage/crear_cuenta.html")

    documento = plantilla.render(dicctionary)

    return HttpResponse(documento)

def faq(request):

    dicctionary = {}
    plantilla = loader.get_template("MainPage/crear_cuenta.html")

    documento = plantilla.render(dicctionary)

    return HttpResponse(documento)

def acerca_de(request):

    dicctionary = {}
    plantilla = loader.get_template("MainPage/crear_cuenta.html")

    documento = plantilla.render(dicctionary)

    return HttpResponse(documento)