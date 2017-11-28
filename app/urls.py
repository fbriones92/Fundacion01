'''
Created on 19 nov. 2017

@author: franklin
'''
from django.conf.urls import url

from app.views import inicio
from django.contrib.auth.urls import urlpatterns



urlpatterns = [
    url(r'^', inicio, name='inicio'),
    
]

#url(r'^actualizar/(?P<persona_id>\d+)/$'