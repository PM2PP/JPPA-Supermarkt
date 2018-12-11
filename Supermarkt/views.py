from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Produkte, Lieferant, Regal
from django_tables2 import RequestConfig
from .Tabelle import LieferantenTable


def startseite(request):
    context = {'Titel': 'JPPA Supermarkt'}
    return render(request=request, template_name='supermarkt/start.html',
                context=context)


def index(request):   
    context = {'produkt': Produkte.objects.all(), 'Titel': 'Produkte/ Sortiment' }
    return render(request=request, template_name='supermarkt/index.html',
                context=context)
        
        
def liefer(request):   
    context = {'lieferant': Lieferant.objects.all(), 'Titel': 'Lieferant' }
    return render(request=request, template_name='supermarkt/liefer.html',
                context=context)

    
def lager(request):
    context = {'regal': Regal.objects.all(), 'Titel': 'Lager'}
    return render(request=request, template_name='supermarkt/regal.html',
                  context=context)

    
def versuch(request):
    context = {'produkt': Produkte.objects.all(), 'Titel': 'Produkte/ Sortiment' }
    return render(request=request, template_name='supermarkt/versuch.html',
                context=context)
