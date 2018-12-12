from django.urls import path

from .views import index, liefer, lager, startseite, versuch, bestand, sortiment

app_name = 'Supermarkt'
urlpatterns = [
    # hey, wenn eine Anfrage an / reinkommt, dann übergebe das der Funktion
    # index aus der views.py
    path('',startseite, name = 'start'),
    path('index/', index, name = 'index'),
    path('liefer/', liefer, name = 'liefer'),
    path('lager/', lager, name = 'lager'),
    path('versuch/', versuch, name = 'versuch'),
    path('bestand/', bestand, name = 'bestand'),
     path('sortiment/', sortiment, name = 'sortiment'),
    
    ]

