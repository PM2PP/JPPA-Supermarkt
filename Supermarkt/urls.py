from django.urls import path

from .views import index, liefer, lager, startseite, versuch

app_name = 'Supermarkt'
urlpatterns = [
    # hey, wenn eine Anfrage an / reinkommt, dann übergebe das der Funktion
    # index aus der views.py
    path('',startseite, name = 'start'),
    path('index/', index, name = 'index'),
    path('liefer/', liefer, name = 'liefer'),
    path('lager/', lager, name = 'lager'),
    path('versuch/', versuch, name = 'versuch'),
    #path('poll/<str:slug>/', PollDetailView.as_view(), name='umfrage-detail'),
   # path('poll/<str:slug>/vote/', vote, name='vote'),
   # path('poll/<str:slug>/results/', ResultsDetailView.as_view(), name='results'),
]
