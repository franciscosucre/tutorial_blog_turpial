# -*- coding: utf-8 -*-
'''
Define las urls que podemos colocar en el navegador para hacer uso de las funcionalidades de nuestra aplicacion

Al colocar una de las siguientes urls en el explorador, ejecturaremos el view asociado a ese url
'''
from django.conf.urls import url

from writer.article import views

urlpatterns = [
  url(r'^$', views.article_list, name='article_list'),
  url(r'^detail/(?P<pk>\d+)$', views.article_detail, name='article_detail'),
  url(r'^new$', views.article_create, name='article_new'),
  url(r'^edit/(?P<pk>\d+)$', views.article_update, name='article_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.article_delete, name='article_delete')
]