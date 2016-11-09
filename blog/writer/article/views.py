# -*- coding: utf-8 -*-
'''
views.py: equivalentes a los actions de struts, estan vinculados a las url de urls.py, cuando
alguien accede a uno de esos url se busca en estos archivos el view correspondiente y se ejecuta
'''
from writer.article.models import Article
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
# import the logging library
import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.urls.base import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Get an instance of a logger
logger = logging.getLogger()

class article_list(LoginRequiredMixin,ListView):
    model = Article
    paginate_by = 2
    def get_queryset(self):
        writer = self.request.user
        qs = Article.objects.filter(writer=writer)
        return qs
    
class article_create(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Article
    fields=['name','content']
    
    def get_success_url(self):
        return (reverse_lazy('article_list') + '?page=1')
    
    def form_valid(self, form):
        writer = self.request.user
        form.instance.writer = writer
        messages.success(self.request,"Haz creado exitosamente el articulo")
        return super(article_create, self).form_valid(form)
    
class article_detail(LoginRequiredMixin,DetailView):
    model = Article

class article_update(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Article
    fields=['name','content']
    
    def get_success_url(self):
        return (reverse_lazy('article_list') + '?page=1')
    
    def form_valid(self, form):
        messages.success(self.request,"Haz actualizado exitosamente el articulo")
        return super(article_update, self).form_valid(form)

class article_delete(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Article
    def get_success_url(self):
        return (reverse_lazy('article_list') + '?page=1')
    
    def delete(self,request,*args, **kwargs):
        messages.success(self.request,"Haz eliminado exitosamente el articulo")
        return super(article_delete,self).delete(request,*args, **kwargs)
    
class Success(TemplateView):
    template_name = "success.html"
