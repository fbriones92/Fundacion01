'''
Created on 20 nov. 2017

@author: franklin
'''
from django.conf.urls import url

from voluntarios.views import home

urlpatterns = [
    url(r'^', home, name='home'),
    
]
