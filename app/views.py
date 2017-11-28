from django.shortcuts import render
from  django.template.context_processors import request
from datetime import datetime
from django.http.request import HttpRequest



def inicio(request):
    return render(request, 'banner.html', {'year':datetime.now().year,})

