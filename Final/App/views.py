from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from App.models import Crear_cuenta
from django.contrib.auth.hashers import make_password, check_password
import logging
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login2(request):
    auxdict = {}
    if request.method == 'POST':
        if request.POST.get('login-hidden') == "login-hidden":
            username = request.POST.get('username-li')
            password = request.POST.get('password-li')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            # A backend authenticated the credentials
                auxdict['rta_login'] = "OK"
            else:
            # No backend authenticated the credentials
                auxdict['rta_login'] = "FAIL"
    return auxdict

def logout2(request):
    logout(request)
    return redirect('/')
def index(request):
    dicctionary = {}
    dicctionary.update(login2(request))
    print(dicctionary)
    
    return render(request,"MainPage/index_hijo.html",dicctionary)

def crear_cuenta(request):
    dicctionary = {}
    dicctionary.update(login2(request))
    print(dicctionary)
    if request.method == 'POST': 
            username = request.POST.get('username', False)
            if User.objects.filter(username=username).exists():
                respuesta = {"mensaje" : "Ya existe usuario."}
                return render(request,'MainPage/crear_cuenta.html',respuesta)
            
            password = request.POST.get('password', False)
            mail = request.POST.get('mail', False)
            if User.objects.filter(email=mail).exists():
                respuesta = {"mensaje" : "Ya existe correo."}
                return render(request,'MainPage/crear_cuenta.html',respuesta)
            createacc =    User.objects.create_user(username, mail, password)
            createacc.save()
            respuesta = {"mensaje" : "Cuenta creada correctamente."}
            return render(request,'MainPage/crear_cuenta.html',respuesta)
    return render(request,'MainPage/crear_cuenta.html', dicctionary)



def actuales(request):

    dicctionary = {}
    rta_login = login2(request)
    dicctionary['rta_login'] = rta_login
    
    
    return render(request,"MainPage/index_hijo.html",dicctionary)

def vencidas(request):

    dicctionary = {}
    rta_login = login2(request)
    dicctionary['rta_login'] = rta_login
    
    
    return render(request,"MainPage/index_hijo.html",dicctionary)

def ganadores(request):

    dicctionary = {}
    rta_login = login2(request)
    dicctionary['rta_login'] = rta_login
    
    
    return render(request,"MainPage/index_hijo.html",dicctionary)

def faq(request):

    dicctionary = {}
    rta_login = login2(request)
    dicctionary['rta_login'] = rta_login
    
    
    return render(request,"MainPage/index_hijo.html",dicctionary)

def acerca_de(request):

    dicctionary = {}
    rta_login = login2(request)
    dicctionary['rta_login'] = rta_login
    
    
    return render(request,"MainPage/index_hijo.html",dicctionary)