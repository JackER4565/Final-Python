from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from App.models import Blog
from django.contrib.auth.models import User
from .forms import AgregarBlog
from django.contrib.auth import login, authenticate
import random
from pathlib import Path

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

def acerca_de(request):
    dicctionary = {}
    return render(request,"acerca_de.html",dicctionary)

def agregar_entrada(request):
    dicctionary = {}
    if request.method == 'POST':
        
        form = AgregarBlog(request.POST, request.FILES)
        if form.is_valid():
            lines = open(Path(__file__).resolve().parent / 'static/facs.txt').read().splitlines()
            myline =random.choice(lines)
            icono = myline
            titulo = form.cleaned_data.get("titulo")
            subtitulo = form.cleaned_data.get("subtitulo")
            texto_corto = form.cleaned_data.get("texto_corto")
            texto_largo = form.cleaned_data.get("texto_largo")
            autor = form.cleaned_data.get("autor")
            activo = 1
            imagen = form.cleaned_data.get("imagen")
            obj = Blog.objects.create(
                icono = icono,
                titulo = titulo,
                imagen = imagen,
                subtitulo = subtitulo,
                texto_corto = texto_corto,
                texto_largo = texto_largo,
                autor = autor,
                activo = activo)
            
            obj.save()
            dicctionary['respuesta_add'] = "Agregado correctamente"
    else:
        form = AgregarBlog()
    dicctionary['form'] = form
    
    return render(request, "agregar_entrada.html", dicctionary)

def actuales(request):

    dicctionary = {}    
    bobjects = Blog.objects.all()
    dicctionary["bobjects"] = bobjects
    return render(request,"actuales.html",dicctionary)

def single_view(request, string):
    dicctionary = {}
    bobjects = Blog.objects.filter(id=string)
    dicctionary["svobj"] = bobjects

    return render(request, "singleview.html", dicctionary)
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

