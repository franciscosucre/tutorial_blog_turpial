# -*- coding: utf-8 -*-
 
from django.test import TestCase
 
from writer.models import Writer
from writer.form import WriterLogin
from writer.form import WriterRegister
from writer.controller import registerWriter
from writer.exceptions import PasswordDifferent
from django.db import IntegrityError
 
###################################################################
#                    BILLETERA_ELECTRONICA FORM
###################################################################
 
class registerWriterFormTestCase(TestCase):
 
    # borde
    def test_registerWriterForm_Vacio(self):
        form_data = {}
        form = WriterRegister(data = form_data)
        self.assertFalse(form.is_valid())
 
    # borde
    def test_registerWriterForm_Sin_Correo(self):
        form_data = {
            'email': None,
            'password': '1234',
            'comfirmPassword': '1234',
            'firstName': 'Prueba',
            'lastName': 'Chevere',
            'pseudonym': 'ChevePrueba',
        }
        form = WriterRegister(data = form_data)
        self.assertFalse(form.is_valid())

    # borde
    def test_registerWriterForm_Sin_Nombre(self):
        form_data = {
            'email': 'prueba@gmail.com',
            'password': '1234',
            'comfirmPassword': '1234',
            'firstName': None,
            'lastName': 'Chevere',
            'pseudonym': 'ChevePrueba',
        }
        form = WriterRegister(data = form_data)
        self.assertFalse(form.is_valid())
        
    # borde
    def test_registerWriterForm_Sin_Apellido(self):
        form_data = {
            'email': 'prueba@gmail.com',
            'password': '1234',
            'comfirmPassword': '1234',
            'firstName': 'Prueba',
            'lastName': None,
            'pseudonym': 'ChevePrueba',
        }
        form = WriterRegister(data = form_data)
        self.assertFalse(form.is_valid())
        
    # borde
    def test_registerWriterForm_Sin_Clave(self):
        form_data = {
            'email': 'prueba@gmail.com',
            'password': None,
            'comfirmPassword': '1234',
            'firstName': 'Prueba',
            'lastName': 'Chevere',
            'pseudonym': 'ChevePrueba',
        }
        form = WriterRegister(data = form_data)
        self.assertFalse(form.is_valid())
        
    # borde
    def test_registerWriterForm_Sin_Pseudonimo(self):
        form_data = {
            'email': 'prueba@gmail.com',
            'password': '1234',
            'comfirmPassword': '1234',
            'firstName': 'Prueba',
            'lastName': 'Chevere',
            'pseudonym': None,
        }
        form = WriterRegister(data = form_data)
        self.assertFalse(form.is_valid())
        
    # borde
    def test_registerWriterForm_Llenado_Exitoso(self):
        form_data = {
            'email': 'prueba@gmail.com',
            'password': '1234',
            'comfirmPassword': '1234',
            'firstName': 'Prueba',
            'lastName': 'Chevere',
            'pseudonym': 'ChevePrueba',
        }
        form = WriterRegister(data = form_data)
        self.assertTrue(form.is_valid())
      
class registerWriterControllerTestCase(TestCase):      
    # borde
    def test_registerWriterController_Claves_Distintas(self):
        form_data = {
            'email': 'prueba@gmail.com',
            'password': '1234',
            'comfirmPassword': '4321',
            'firstName': 'Prueba',
            'lastName': 'Chevere',
            'pseudonym': 'ChevePrueba',
        }
        form = WriterRegister(form_data)
        form.is_valid()
        self.assertRaises(PasswordDifferent,registerWriter,form=form)
        
    # No logro hacer funcionar esto, no se porque, en funcionamiento real funciona
    def test_registerWriterController_Duplicate_User(self):
        form_data = {
            'email': 'prueba@gmail.com',
            'password': '1234',
            'comfirmPassword': '1234',
            'firstName': 'Prueba',
            'lastName': 'Chevere',
            'pseudonym': 'ChevePrueba',
        }
        form = WriterRegister(form_data)
        form.is_valid()
        registerWriter(form)
        form_data = {
            'email': 'prueba@gmail.com',
            'password': '1234',
            'comfirmPassword': '1234',
            'firstName': 'Prueba',
            'lastName': 'Duplicada',
            'pseudonym': 'CheveDuplicada',
        }
        form = WriterRegister(form_data)
        form.is_valid()
        self.assertRaises(IntegrityError,registerWriter,form=form)
