from django.shortcuts import render
from .models import Produkte, Lieferant, Regal, Lager, Sortiment
from django.template.context_processors import request


def startseite(request):
    context = {'Titel': 'JPPA Supermarkt'}
    return render(request=request, template_name='supermarkt/start.html',
                context=context)


def index(request):   
    context = {'produkt': Produkte.objects.all(), 'Titel': 'Bestand Supermarkt' }
    return render(request=request, template_name='supermarkt/index.html',
                context=context)
        
        
def liefer(request):   
    context = {'lieferant': Lieferant.objects.all(), 'Titel': 'Lieferant' }
    return render(request=request, template_name='supermarkt/liefer.html',
                context=context)

    
def lager(request):
    context = {'lager': Lager.objects.all(), 'Titel': 'Bestand Lager'}
    return render(request=request, template_name='supermarkt/lager.html',
                  context=context)


def bestand(request):
       context = {'Titel': 'Bestand'}
       return render(request=request, template_name='supermarkt/bestand.html',
                context=context)


def sortiment(request):
         context = {'sortiment': Sortiment.objects.all(), 'Titel': 'Sortiment'}
         return render(request=request, template_name='supermarkt/sortiment.html',
                  context=context)


def versuch(request):
    context = {'produkt': Produkte.objects.all(), 'Titel': 'Produkte/ Sortiment' }
    return render(request=request, template_name='supermarkt/versuch.html',
                context=context)
