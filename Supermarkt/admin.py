from django.contrib import admin

from .models import Produkte, Lieferant, Regal, Lager

admin.site.register(Produkte)
admin.site.register(Lieferant)
admin.site.register(Regal)
admin.site.register(Lager)