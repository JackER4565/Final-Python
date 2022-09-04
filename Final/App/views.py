from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.models import Crear_cuenta
from django.contrib.auth.hashers import make_password, check_password
import logging
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    dicctionary = {}

    
    if request.method == 'POST':
            username = request.POST.get('username-li')
            encryptedpassword=make_password(request.POST.get('password-li'))
            
            print("post index")
            print(username)
            print(Crear_cuenta.objects.filter(username=username).exists())
            if Crear_cuenta.objects.filter(username=username).exists():
                print("llegue primer if")
                data = Crear_cuenta.objects.filter(username=username).values('password')
                print(data)
                data = str(data)[25:-4]
                print(data)
                print(encryptedpassword)
                print(check_password(data, encryptedpassword))
                user = Crear_cuenta.objects.get(username=username)
                print(user)
                user.check_password(password)
                # <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>
                if check_password(data, encryptedpassword):
                    print("llegue segundo  if")
                    dicctionary['rta_login'] = "OK"
            dicctionary['rta_login'] = "FAIL"

    return render(request,"MainPage/index_hijo.html",dicctionary)

def crear_cuenta(request):

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