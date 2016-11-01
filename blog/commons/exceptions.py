# -*- coding: utf-8 -*-
'''
exceptions.py: En este archivo guardamos las distintas clases de excepciones personalizadas que utilizaremos
durante la ejecucion de nuestra aplicacion
'''
from django.utils.translation import ugettext as _

class UnknownError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return _("Please Call The Administrator")