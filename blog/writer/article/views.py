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
# Get an instance of a logger
logger = logging.getLogger()

class article_list(LoginRequiredMixin,ListView):
    model = Article
    def get_queryset(self):
        writer = self.request.user
        qs = Article.objects.filter(writer=writer)
        return qs
    
class article_create(LoginRequiredMixin,CreateView):
    model = Article
    fields=['name','content']
    success_url = '/writer/article'
    
    def form_valid(self, form):
        writer = self.request.user
        form.instance.writer = writer
        return super(article_create, self).form_valid(form)
    
class article_detail(LoginRequiredMixin,DetailView):
    model = Article
    def dispatch(self, *args, **kwargs): 
        self.article_id = kwargs['pk'] 
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs) 

class article_update(LoginRequiredMixin,UpdateView):
    model = Article
    fields=['name','content']
    success_url = '/writer/article'
    
    def dispatch(self, *args, **kwargs): 
        self.article_id = kwargs['pk'] 
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs) 
    
    def form_valid(self, form): 
        form.save() 
        return super(article_update, self).form_valid(form)
        #return HttpResponse(render_to_string('article/success.html', {'article': article}))

class article_delete(LoginRequiredMixin,DeleteView):
    model = Article
    success_url = '/writer/article'
    
class Success(TemplateView):
    template_name = "success.html"
