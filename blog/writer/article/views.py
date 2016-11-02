# -*- coding: utf-8 -*-
'''
views.py: equivalentes a los actions de struts, estan vinculados a las url de urls.py, cuando
alguien accede a uno de esos url se busca en estos archivos el view correspondiente y se ejecuta
'''
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from writer.article.models import Article
from sys import exc_info
from commons.exceptions import UnknownError
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger()

class articleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name','content']
# Se tuvo que utilizar esto para que funcione en chrome
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Define que se necesita hacer login para ingresar a este view
@login_required  
# Vista para listar los proyectos
def article_list(request, template_name='article_list.html'):
    try: 
        articles = Article.objects.all().filter(writer=request.user.writer)
        data = {}
        data['object_list'] = articles
        return render(request, template_name, data)
    except:
        message = str(UnknownError())
        logger.exception(message)
        return render(
            request,
            'article_list.html',
            { "object_list" : None
             , "color"   : "red"
            , 'message' : message})
        
# Se tuvo que utilizar esto para que funcione en chrome
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Define que se necesita hacer login para ingresar a este view
@login_required  
def article_detail(request, pk, template_name='article_detail.html'):
    try: 
        # article = get_object_or_404(Article, pk=pk)
        article = get_object_or_404(Article, pk=pk)
        data = {}
        data['article'] = article
        return render(request, template_name, data)
    except:
        message = str(UnknownError())
        logger.exception(message)
        return render(
            request,
            'article_detail.html',
            { "article" : None
             , "color"   : "red"
            , 'message' : message})

# Se tuvo que utilizar esto para que funcione en chrome
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Define que se necesita hacer login para ingresar a este view
@login_required  
# Vista para crear un proyecto
def article_create(request, template_name='article_form.html'):
    try: 
        # Obtenemos los datos del form
        form = articleForm(request.POST or None)
        # Validamos el formulario
        if form.is_valid():
            # Creamos un nuevo proyecto con lso datos que se nos ieron
            newarticle = Article(writer=request.user.writer,
                                 name=form.cleaned_data['name'],
                                 content=form.cleaned_data['content']
                                 )
            # Guardamos el proyecto en base de datos
            newarticle.save()
            # Nos redirigimos al url article_list
            return redirect('article_list')
        return render(request, template_name, {'form':form})
    except:
        message = str(UnknownError())
        logger.exception(message)
        return render(
            request,
            'article_form.html',
            { "object_list" : None
             , "color"   : "red"
            , 'message' : message})
# Se tuvo que utilizar esto para que funcione en chrome
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Define que se necesita hacer login para ingresar a este view
@login_required  
# Vista para actualizar un proyecto
# Este view recibe como argumento la llave primaria del proyecto a editar
def article_update(request, pk, template_name='article_form.html'):
    try: 
        article = get_object_or_404(Article, pk=pk)
        form = articleForm(request.POST or None, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
        return render(request, template_name, {'form':form})
    except:
        message = str(UnknownError())
        logger.exception(message)
        return render(
            request,
            'article_form.html',
            { "object_list" : None
             , "color"   : "red"
            , 'message' : message})
# Se tuvo que utilizar esto para que funcione en chrome
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# Define que se necesita hacer login para ingresar a este view
@login_required  
# Vista para borrar un proyecto
def article_delete(request, pk, template_name='article_confirm_delete.html'):
    try: 
        article = get_object_or_404(Article, pk=pk)    
        if request.method=='POST':
            article.delete()
            return redirect('article_list')
        return render(request, template_name, {'object':article})
    except:
        message = str(UnknownError())
        logger.exception(message)
        return render(
            request,
            'article_confirm_delete.html',
            { "object_list" : None
             , "color"   : "red"
            , 'message' : message})