# -*- coding: utf-8 -*-
'''
Define las urls que podemos colocar en el navegador para hacer uso de las funcionalidades de nuestra aplicacion

Al colocar una de las siguientes urls en el explorador, ejecturaremos el view asociado a ese url
'''
from django.conf.urls import url
from commons.views import Index,Home,About
from django.contrib.auth import views as auth_views

# Este error es raro, en django funciona
urlpatterns = [
    url(r'^index', Index.as_view(),name = 'Index'),
    url(r'^$', Index.as_view(),name = 'Index'),
    url(r'^login/$', auth_views.login,name = 'login') ,
    url(r'^logout/$', auth_views.logout,name = 'logout'),
    url(r'^password_change/$', auth_views.password_change,name = 'password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done,name = 'password_change_done'),
    url(r'^password_reset/$', auth_views.password_reset,name = 'password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,name = 'password_reset_done'),
    url(r'^password_reset/$', auth_views.password_reset,name = 'password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm,name = 'password_reset_confirm'),
    url(r'^reset/done$', auth_views.password_reset_complete,name = 'password_reset_complete'),
    url(r'^home$', Home.as_view(),name = 'Home'),
    url(r'^home/$', Home.as_view(),name = 'Home'),
    url(r'^about$', About.as_view(),name = 'About')
]
