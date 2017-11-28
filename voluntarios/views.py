from django.shortcuts import render
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    templates = 'voluntario_master.html'
    return render(request, templates)
