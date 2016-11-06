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
    
    widgets = {
            'username': forms.TextInput(attrs={'class' : 'form-control'}),
            'first_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.TextInput(attrs={'class' : 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class' : 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class' : 'form-control'}),
        }
    
    
    class Meta:
        model = Writer
        fields = ("username", "first_name","last_name","email", "password1", "password2","pseudonym")

