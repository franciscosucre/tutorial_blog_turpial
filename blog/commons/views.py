'''
views.py: equivalentes a los actions de struts, estan vinculados a las url de urls.py, cuando
alguien accede a uno de esos url se busca en estos archivos el view correspondiente y se ejecuta
'''
from django.shortcuts import render
from commons.exceptions import UnknownError
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.cache import cache_control
from sys import exc_info

from django.shortcuts import (redirect)
from django.contrib.auth import authenticate
from django.contrib.auth import login
from writer.form import (WriterLogin)
from writer.exceptions import (NotAWriter,CouldNotAuthenticate)
from writer.models import Writer
from django.core.urlresolvers import reverse
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
        logger.error(message)
        logger.error(exc_info[0])
        return render(
            request,
            'index.html')
        
def loginView(request):
    # Envolvemos el codigo en manejo de errores
    try:
        if request.user.is_authenticated():
            return redirect(reverse('Home'))
        # Creamos un formulario de registro
        loginForm = WriterLogin()
        # Si estamos haciendo un submit de un formulario
        if request.method == 'POST':
            loginForm = WriterLogin(request.POST)
            if loginForm.is_valid():
                # Autenticamos los credenciales
                Loggeduser = authenticate(username=loginForm.cleaned_data['email'], password=loginForm.cleaned_data['password'])
                # Verificamos que el usuario logro autenticarse
                if not Loggeduser:
                    raise CouldNotAuthenticate
                # Buscamos su informacion de escritor
                writerInfo=Writer.objects.get(user=Loggeduser)
                # Verificamos que es un escritor
                if not writerInfo:
                    raise NotAWriter
                # Ejecutamos el inicio de session
                login(request, Loggeduser)
                # Renderizamos el html con los datos del nuevo escritor
                # Esto sirve para redirigir
                return redirect(reverse('Home'))

        # Renderizamos el html enviando solo el form
        return render(
            request,
            'login.html',
            { 'loginForm' : loginForm 
            , "color"   : None
            , 'message' :None})
    # Si recibimos cualquier otra excepcion
    except CouldNotAuthenticate:
        message = str(CouldNotAuthenticate())
        logger.error(message)
        return render(
            request,
            'login.html',
            { 'loginForm' : loginForm 
            , "color"   : "red"
            , 'message' :message})
    except NotAWriter:
        message = str(NotAWriter())
        logger.error(message)
        return render(
            request,
            'login.html',
            { 'loginForm' : loginForm 
            , "color"   : "red"
            , 'message' :message})
    except:
        logger.error(message)
        logger.error(exc_info[0])
        message = str(UnknownError())
        return render(
            request,
            'login.html',
            { 'loginForm' : loginForm 
            , "color"   : "red"
            , 'message' :message})

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
        logger.error(message)
        logger.error(exc_info[0])
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
        logger.error(message)
        logger.error(exc_info[0])
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
