# -*- coding: utf-8 -*-
'''
Define las urls que podemos colocar en el navegador para hacer uso de las funcionalidades de nuestra aplicacion

Al colocar una de las siguientes urls en el explorador, ejecturaremos el view asociado a ese url
'''
from django.conf.urls import url, include

from writer import views


# Este error es raro, en django funciona
urlpatterns = [
    url(r'^RegisterWriter$', views.RegisterWriter.as_view(),name = 'RegisterWriter'),
    url(r'^register_done', views.RegisterWriterDone.as_view(),name = 'RegisterWriterDone'),
    url(r'^article/', include('writer.article.urls')),
]