# -*- coding: utf-8 -*-
'''
form.py: En este archivo construiremos los formularios que utilizara nuestra aplicacion
'''
from django.contrib.auth.forms import UserCreationForm
from django import forms
from writer.models import Writer


class WriterRegister(UserCreationForm):
    '''
    Campos
    '''
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Writer
        fields = ("username", "first_name","last_name","email", "password1", "password2","pseudonym")

