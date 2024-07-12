from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm,CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages



# Create your views here.
def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'inicio.html')


def ingreso(request):
    return render(request, 'ingreso.html')



def registro(request):
    data= {
        'form': CustomUserCreationForm()
        }
    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password"])
            login(request,user)
            messages.success(request,"te has registrado correctamente")
            return redirect (to="menuprincipal")
        data["form"]=formulario
    return render(request, 'registration/registro.html', data)

@login_required
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
