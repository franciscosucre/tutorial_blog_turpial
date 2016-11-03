# -*- coding: utf-8 -*-
'''
views.py: equivalentes a los actions de struts, estan vinculados a las url de urls.py, cuando
alguien accede a uno de esos url se busca en estos archivos el view correspondiente y se ejecuta
'''
from django.shortcuts import (render)
from writer.form import (WriterRegister)
from writer.exceptions import (PasswordDifferent)
from commons.exceptions import UnknownError
from sys import exc_info
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

def registerWriterView(request):
    # Envolvemos el codigo en manejo de errores
    try:
        # Creamos un formulario de registro
        registerForm = WriterRegister()
        # Si estamos haciendo un submit de un formulario
        if request.method == 'POST':
            registerForm = WriterRegister(request.POST)
            if registerForm.is_valid():
                # Registramos al escritor
                newWriter = registerForm.save(True)
                # Renderizamos el html con los datos del nuevo escritor
                return render(
                    request,
                    'RegisterWriter.html',
                    { "newUser"      : newWriter
                    , "registerForm"    : registerForm
                    , "newWriter" : newWriter
                    , "color"   : "green"
                    , 'message' : "Se realizo el registro satisfactoriamente."
                    }
                )
        # Renderizamos el html enviando solo el form
        return render(
                    request,
                    'RegisterWriter.html',
                    { "newUser"      : None
                    , "registerForm"    : registerForm
                    , "newWriter" : None
                    , "color"   : "green"
                    , 'message' : "Por favor rellene el formulario"
                    }
                )
        
    # Si recibimos nuestra excepcion personalizada
    except PasswordDifferent:
        message = str(PasswordDifferent())
        logger.error(message)
        return render(
            request,
            'RegisterWriter.html',
            { "newUser"      : None
             ,'registerForm' : registerForm
             , "newWriter" : None
             , "color"   : "red"
            , 'message' : message})
    # Si recibimos cualquier otra excepcion
    except:
        message = str(UnknownError())
        logger.exception(message)
        logger.exception(exc_info()[0])
        return render(
            request,
            'RegisterWriter.html',
            { "newUser"      : None
             ,'registerForm' : registerForm
             , "newWriter" : None
             , "color"   : "red"
            , 'message' : message})

