'''
views.py: equivalentes a los actions de struts, estan vinculados a las url de urls.py, cuando
alguien accede a uno de esos url se busca en estos archivos el view correspondiente y se ejecuta
'''
from django.shortcuts import render
from commons.exceptions import UnknownError
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from sys import exc_info

from django.contrib.auth import logout
from django.contrib import messages
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

def indexView(request):
    # Envolvemos el codigo en manejo de errores
    try:
        # Renderizamos el html enviando solo el form
        return render(
            request, 'index.html')
        
    # Si recibimos cualquier otra excepcion
    except:
        message = str(UnknownError())
        logger.exception(message)
        logger.exception(exc_info()[0])
        return render(
            request,
            'index.html')
        
# Se tuvo que utilizar esto para que funcione en chrome
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Define que se necesita hacer login para ingresar a este view
@login_required       
def logoutView(request):
    # Envolvemos el codigo en manejo de errores
    try:
        logout(request)
        messages.success(request, 'Te has desconectado con exito.')
        # Renderizamos el html enviando solo el form
        return render(
            request, 'logout.html')
    # Si recibimos cualquier otra excepcion
    except:
        message = str(UnknownError())
        logger.exception(message)
        logger.exception(exc_info()[0])
        return render(
            request,
            'logout.html')
        
# Se tuvo que utilizar esto para que funcione en chrome
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Define que se necesita hacer login para ingresar a este view
@login_required   
def homeView(request):
    # Envolvemos el codigo en manejo de errores
    try:
        # Obtenemos al usuario actual
        current_user = request.user
        # Renderizamos el html enviando solo el form
        return render(
            request,
            'home.html',
            { "color"   : 'black'
            , 'id' :current_user.id
            , 'first_name' :current_user.first_name
            , 'last_name' :current_user.last_name
            , 'email' :current_user.email
            , 'pseudonym' :current_user.pseudonym
            , 'message' :None
            })
    except:
        message = str(UnknownError())
        logger.exception(message)
        logger.exception(exc_info()[0])
        return render(
            request,
            'home.html',
            { "color"   : "red"
            , 'id' :None
            , 'first_name' :None
            , 'last_name' :None
            , 'email' :None
            , 'pseudonym' :None
            , 'message' :message})
