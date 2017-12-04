'''
Created on 20 nov. 2017

@author: franklin
'''
from django.conf.urls import url

from voluntarios.views import  voluntarios, fundacion, voluntario, update

urlpatterns = [
    #url(r'^', home, name='home'),
    url(r'^/fundacion/', fundacion, name='funda'),
    url(r'^/voluntarios/$', voluntarios, name='voluntarios'),
    url(r'^/voluntarios/crear/$', voluntario, name="voluntario"),
    url(r'^/voluntarios/crear/(?P<voluntario_id>\d+)$', voluntario, name="voluntario"),
    url(r'^/voluntarios/deshabilitar/(?P<voluntario_id>\d+)$', update, name='update'),
       
]
