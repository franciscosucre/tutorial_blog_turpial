# -*- coding: utf-8 -*-
'''
Define las urls que podemos colocar en el navegador para hacer uso de las funcionalidades de nuestra aplicacion

Al colocar una de las siguientes urls en el explorador, ejecturaremos el view asociado a ese url
'''
from django.conf.urls import url

from writer.article import views

urlpatterns = [
  url(r'^(?P<page>\d*)?$', views.article_list.as_view(), name='article_list'),
  url(r'^detail/(?P<pk>\d+)$', views.article_detail.as_view(), name='article_detail'),
  url(r'^new$', views.article_create.as_view(), name='article_new'),
  url(r'^edit/(?P<pk>\d+)$', views.article_update.as_view(), name='article_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.article_delete.as_view(), name='article_delete'),
  url(r'^success/$', views.Success.as_view(), name='success')
]

