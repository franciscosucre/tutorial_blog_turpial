# -*- coding: utf-8 -*-
'''
form.py: En este archivo construiremos los formularios que utilizara nuestra aplicacion
'''
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from writer.models import Writer

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class WriterRegister(UserCreationForm):
    '''
    Campos
    '''
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    
    pseudonym = forms.CharField(
        required   = True,
        label      = _('pseudonym'),
        widget = forms.TextInput(attrs =
            { 'class'      : 'form-control'
            , 'placeholder' : _('pseudonym')
            }
        )
    )
    
    class Meta:
        model = User
        fields = ("username", "first_name","last_name","email", "password1", "password2")
        
    def save(self, commit=True):
        with transaction.atomic():
            user = super(UserCreationForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            writer = Writer(
                user = user,
                pseudonym = self.cleaned_data['pseudonym']
                )
            user.save()
            writer.save()
            return writer
    
