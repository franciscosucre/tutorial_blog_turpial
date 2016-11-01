# -*- coding: utf-8 -*-
'''
Define las urls que podemos colocar en el navegador para hacer uso de las funcionalidades de nuestra aplicacion

Al colocar una de las siguientes urls en el explorador, ejecturaremos el view asociado a ese url
'''
from django.conf.urls import url
from commons.views import indexView, loginView,logoutView,homeView

# Este error es raro, en django funciona
urlpatterns = [
    url(r'^index', indexView,name = 'Index'),
    url(r'^$', indexView,name = 'Index'),
    url(r'^login$', loginView,name = 'Login'),
    url(r'^logout$', logoutView,name = 'Logout'),
    url(r'^home$', homeView,name = 'Home')
]