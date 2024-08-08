from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .forms import Loginform,register
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Usuario, AuthUser




# Create your views here.
def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'inicio.html')

def consejos(request):
    return render(request, 'consejos.html')

def videos(request):
    return render(request, 'videos.html')

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


# def registro(request):
#     if request.method == 'POST':
#         print(request.POST)
#         formulario = register(request.POST)
#         if formulario.is_valid():
#             new_user = formulario.save(commit=False)
#             new_user.set_password(formulario.cleaned_data['password'])
#             new_user.save()
#             nombre = formulario.cleaned_data.get('nombre')
#             correo_u = formulario.cleaned_data.get('email')
#             subject = 'Registro en bienestar a la mano'
#             message = f'{nombre}, ¡Bienvenid@ a Bienestar a la mano'
#             from_email = settings.EMAIL_HOST_USER
#             recipient_list = [correo_u]

#             send_mail(subject, message, from_email, recipient_list)

#             messages.success(request, "Registro exitoso. Hemos enviado un correo de bienvenida a tu dirección.")
#             return redirect('login')
#         return render(request, 'registration/registro.html', {'formulario':formulario,'auth_error': 'Autenticación fallida'})
#     else:
#         formulario= register()
#     return render(request, 'registration/registro.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        print(request.POST)
        formulario = register(request.POST)
        if formulario.is_valid():
            new_user = formulario.save(commit=False)
            new_user.set_password(formulario.cleaned_data['password'])
            new_user.save()

            # Obtenemos el nombre y correo del formulario
            username = formulario.cleaned_data.get('username')
            correo_u = formulario.cleaned_data.get('email')

            subject = 'Registro en bienestar a la mano'
            message = f'{username}, ¡Bienvenid@ a Bienestar a la mano!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [correo_u]

            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, "Registro exitoso. Hemos enviado un correo de bienvenida a tu dirección.")
            return redirect('login')
        return render(request, 'registration/registro.html', {'formulario':formulario,'auth_error': 'Autenticación fallida'})
    else:
        formulario = register()
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
