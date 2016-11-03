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
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView

# import the logging library
import logging
from django.contrib.contenttypes import fields
# Get an instance of a logger
logger = logging.getLogger()

class articleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name','content']

class article_list(ListView):
    model = Article
    def get_queryset(self):
        writer = self.request.user
        qs = Article.objects.filter(writer=writer)
        return qs
    
class article_create(CreateView):
    model = Article
    fields=['name','content']
    success_url = '/writer/article'
    
    def form_valid(self, form):
        writer = self.request.user
        form.instance.writer = writer
        return super(article_create, self).form_valid(form)
    
class article_detail(DetailView):
    model = Article

class article_update(UpdateView):
    model = Article
    fields=['name','content']
    success_url = '/writer/article'

class article_delete(DeleteView):
    model = Article
    success_url = '/writer/article'
