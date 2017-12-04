# -*- coding: utf-8 -*-
from django.shortcuts import render
#from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from voluntarios.models import Voluntario
from django.urls.base import reverse
from voluntarios.forms import VoluntarioForm
from django.db.models import Q

@login_required(login_url='login')
def fundacion (request):
    templates = 'voluntario/fundacion.html'
    return render (request, templates)

@login_required(login_url='login')
def voluntarios(request):
    templates = 'voluntario/voluntarios.html'
    voluntarios = Voluntario.objects.filter(
                Q(estado = Voluntario.ESTADO_ACTIVO))

    data = {
            'voluntarios': voluntarios,
            
        }
    return render(request, templates, data)


@login_required(login_url='login')
def voluntario(request, voluntario_id = None):
    template = 'voluntario/voluntario_crear.html'
    form = VoluntarioForm()
    voluntario = None
    
    if voluntario_id is not None:
        voluntario = Voluntario.objects.get(id = voluntario_id)
        form = VoluntarioForm(instance = voluntario)
            
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, request.FILES, instance = voluntario)
        (form.data)
        if form.is_valid():
            print(form.cleaned_data)
            voluntario = form.save()
            return HttpResponseRedirect(reverse('voluntarios'))
        
    data = {
            'form':form,
            
        }
    return render(request, template, data)


@login_required(login_url='login')
def update(request, voluntario_id = None):
    voluntario = Voluntario.objects.get(id = voluntario_id )
    voluntario.estado = "1"
    voluntario.save()
    return HttpResponseRedirect(reverse('voluntarios'))






