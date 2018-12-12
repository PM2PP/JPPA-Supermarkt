from django.db import models
from djmoney.models.fields import MoneyField


class Produkte(models.Model):
    Produkt = models.CharField(max_length=256)
    Kategorie = models.CharField(max_length=256)
    Hersteller = models.CharField(max_length=256)
    Lieferant = models.ForeignKey(to='Lieferant', on_delete=models.CASCADE)
    Preis = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    Standort = models.ForeignKey(to='Regal', on_delete=models.CASCADE) 
    Bestand = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "Produkt: {0}, Hersteller: {1}, Lieferant: {2}, Preis: {3}".format(self.Produkt, self.Hersteller, self.Lieferant, self.Preis)


class Sortiment(models.Model):
    Produkt = models.CharField(max_length=256)
    Kategorie = models.CharField(max_length=256)
    Preis = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    Lieferant = models.ForeignKey(to='Lieferant', on_delete=models.CASCADE)
    
    def __str__(self):
        return "Produkt: {0}, Kategorie {1}, Preis: {2}".format(self.Produkt, self.Kategorie, self.Lieferant, self.Preis)


class Lieferant(models.Model):
    Name = models.CharField(max_length=256)
    LiefernatenNr = models.IntegerField(default=0, unique=True)
    
    def __str__(self):
        return "{0}, LieferantenNr:  {1} ".format(self.Name, self.LiefernatenNr)
    
class Lager(models.Model): 
    Produkt = models.CharField(max_length=256)
    Kategorie = models.CharField(max_length=256)
    Hersteller = models.CharField(max_length=256)
    Lieferant = models.ForeignKey(to='Lieferant', on_delete=models.CASCADE)
    Preis = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
    Standort = models.ForeignKey(to='Regal', on_delete=models.CASCADE) 
    Bestand = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "Produkt: {0}, Hersteller: {1}, Lieferant: {2}, Preis: {3}".format(self.Produkt, self.Hersteller, self.Lieferant, self.Preis)

    
class Regal(models.Model):
    Bezeichnung = models.CharField(max_length=256)
    Kapazitaet = models.IntegerField(default=0)
    Standort = models.IntegerField(default=0)
    
    def __str__(self):
        return "{0} ".format(self.Bezeichnung)   