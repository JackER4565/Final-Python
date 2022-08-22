from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):

    dicctionary = {}
    plantilla = loader.get_template("MainPage/index.html")

    documento = plantilla.render(dicctionary)

    return HttpResponse(documento)