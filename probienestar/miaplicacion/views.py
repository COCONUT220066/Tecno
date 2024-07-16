from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .forms import Loginform,register




# Create your views here.
def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'inicio.html')


def login(request):
    if request.method=='POST':
        print(request.POST)
        formulario= Loginform(request.POST)
        if formulario.is_valid():
            cd = formulario.cleanead_data
            username= formulario.cleaned_data["username"]
            password=formulario.cleaned_data["password"]
            user =authenticate (request, username=username, password=password)
        if user is not None:
            if user.is__activate:
                login(request= user)
        else: 
            return render(request, 'registration/login.html' , {'formulario':formulario, 'error': 'Usuario o contraseña incorrectos'} )
    else:
        formulario=Loginform()
        return render(request, 'resgistration/login.html', {'formulario': formulario})
            
def registro(request):
    if request.method == 'POST':
        print(request.POST)
        formulario = register(request.POST)
        if formulario.is_valid():
            new_user = formulario.save(commit=False)
            new_user.set_password(formulario.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        return render(request, 'registration/registro.html', {'formulario':formulario,'auth_error': 'Autenticación fallida'})
    else:
        formulario= register()
    return render(request, 'registration/registro.html', {'formulario': formulario})



def menuprincipal(request):
    return render(request, 'menuprincipal.html')

def recuperar(request):
    return render(request, 'recuperar.html')

def agenda(request):
    return render(request, 'agenda.html')


@login_required
def informacion(request):
    return render(request, 'informacion.html')

def contacto(request):
    return render(request, 'contacto.html')
