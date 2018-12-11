'''
Created on 10 Dec 2018

@author: PRitter
'''

import django_tables2 as tables
from .models import Lieferant


class LieferantenTable(tables.Table):
    class Meta:
        model = Lieferant
        template_name = 'django_tables2/bootstrap.html'