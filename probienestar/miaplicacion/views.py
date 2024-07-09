from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

# Create your views here.
def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'inicio.html')

def ingreso(request):
    return render(request, 'ingreso.html')

def registro(request):
    return render(request, 'registro.html')

def menuprincipal(request):
    return render(request, 'menuprincipal.html')

def recuperar(request):
    return render(request, 'recuperar.html')

def agenda(request):
    return render(request, 'agenda.html')

def contacto(request):
    return render(request, 'contacto.html')

def sintomas(request):
    return render(request, 'sintomas.html')

def informacion(request):
    return render(request, 'informacion.html')
