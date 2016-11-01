# -*- coding: utf-8 -*-
'''
Define las urls que podemos colocar en el navegador para hacer uso de las funcionalidades de nuestra aplicacion

Al colocar una de las siguientes urls en el explorador, ejecturaremos el view asociado a ese url
'''
from django.conf.urls import url, include

from writer import views


# Este error es raro, en django funciona
urlpatterns = [
    url(r'^RegisterWriter$', views.registerWriterView,name = 'RegisterWriter'),
    url(r'^article/', include('writer.article.urls')),
]