# -*- coding: utf-8 -*-
'''
controller.py: En este archivo guardaremos funciones que seran utilizadas en la aplicacion, es una buena practica
encapsular todo el procedimiento de un view en un controller
'''
from writer.models import Writer
from commons.constants import WRITER
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.models import Group
from writer.exceptions import (PasswordDifferent)
def registerWriter(form):
    # Envolvemos el codigo en manejo de errores
    try:
        # Iniciamos una transaccion para asegurar que los procedimientos se cumplan completos
        # o no se cumple ninguno
        with transaction.atomic():
            # Verificamos si las dos contrasenas son iguales
            if form.cleaned_data['password'] != form.cleaned_data['comfirmPassword']:
                # Levantamos una excepcion personalizada
                raise PasswordDifferent
        
            newUser = User.objects.create_user(
                username = form.cleaned_data['email'],
                first_name=form.cleaned_data['firstName'], 
                last_name=form.cleaned_data['lastName'], 
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
                )
            newUser.save()
            
            newWriter = Writer(
                user = newUser,
                pseudonym = form.cleaned_data['pseudonym']
                )
            
            newWriter.save()
            return newWriter
    except:
        raise