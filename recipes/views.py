# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('pagina sobre') 