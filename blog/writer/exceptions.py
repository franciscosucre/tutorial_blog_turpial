# -*- coding: utf-8 -*-
'''
exceptions.py: En este archivo guardamos las distintas clases de excepciones personalizadas que utilizaremos
durante la ejecucion de nuestra aplicacion
'''
from django.utils.translation import ugettext as _

class PasswordDifferent(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return _("Both Password Must Be The Same")

class CouldNotAuthenticate(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return _("The Email And Password Combination Does Not Match")

class NotAWriter(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return _("You Are Not Registred As A Writer")