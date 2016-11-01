# -*- coding: utf-8 -*-
'''
form.py: En este archivo construiremos los formularios que utilizara nuestra aplicacion
'''
from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _

class WriterLogin(forms.Form):
    '''
    Validadores
    '''
    password_validator = RegexValidator(
        regex   = '^[a-zA-Z0-9]+$',
        message = 'El PIN solo puede contener cuatro caracteres numéricos.'
    )
    
    email = forms.EmailField(
        required   = True,
        label      = _('email'),
        widget = forms.EmailInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : _('email')
            }
        )
    )
    '''
    Campos
    '''
    password = forms.CharField(
        required   = True,
        label      = _('password'),
        validators = [password_validator],
        widget = forms.PasswordInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : _('password')
            }
        )
    )
    
class WriterRegister(forms.Form):
    '''
    Validadores
    '''
    password_validator = RegexValidator(
        regex   = '^[a-zA-Z0-9]+$',
        message = 'El PIN solo puede contener cuatro caracteres numéricos.'
    )
     
    firstNameValidator = RegexValidator(
        regex   = '^[a-zA-ZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ\'][a-zA-ZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ\'  ]*$',
        message = 'El nombre no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
    )
    
    lastNameValidator = RegexValidator(
        regex   = '^[a-zA-ZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ\'][a-zA-ZÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ\'  ]*$',
        message = 'El apellido no puede iniciar con espacio en blanco ni contener números ni caracteres desconocidos.'
    )
    '''
    Campos
    '''
    email = forms.EmailField(
        required   = True,
        label      = _('email'),
        widget = forms.EmailInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : _('email')
            }
        )
    )
    
    password = forms.CharField(
        required   = True,
        label      = _('password'),
        validators = [password_validator],
        widget = forms.PasswordInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : _('password')
            }
        )
    )
 
    comfirmPassword = forms.CharField(
        required   = True,
        label      = _('comfirmPassword'),
        validators = [password_validator],
        widget = forms.PasswordInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : _('comfirmPassword')
            }
        )
    )
        
    firstName = forms.CharField(
        required   = True,
        label      = _('firstName'),
        validators = [firstNameValidator],
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : _('firstName')
            , 'pattern'     : firstNameValidator.regex.pattern
            , 'message'     : firstNameValidator.message
            }
        )
    )

    lastName = forms.CharField(
        required   = True,
        label      = _('lastName'),
        validators = [lastNameValidator],
        widget = forms.TextInput(attrs =
            { 'class'      : 'form-control'
            , 'placeholder' : _('lastName')
            , 'pattern'     : lastNameValidator.regex.pattern
            , 'message'     : lastNameValidator.message
            }
        )
    )
    
    pseudonym = forms.CharField(
        required   = True,
        label      = _('pseudonym'),
        validators = [lastNameValidator],
        widget = forms.TextInput(attrs =
            { 'class'      : 'form-control'
            , 'placeholder' : _('pseudonym')
            , 'pattern'     : lastNameValidator.regex.pattern
            , 'message'     : lastNameValidator.message
            }
        )
    )