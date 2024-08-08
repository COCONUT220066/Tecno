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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import Loginform

def login(request):
    if request.method == 'POST':
        formulario = Loginform(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('menuprincipal')  # Redirige a la página de inicio o donde prefieras
                else:
                    messages.error(request, 'La cuenta está desactivada.')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')

    else:
        formulario = Loginform()

    return render(request, 'registration/login.html', {'formulario': formulario})



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

# def registro(request):
#     if request.method == 'POST':
#         print(request.POST)
#         formulario = register(request.POST)
#         if formulario.is_valid():
#             new_user = formulario.save(commit=False)
#             new_user.set_password(formulario.cleaned_data['password'])
#             new_user.save()

#             # Obtenemos el nombre y correo del formulario
#             username = formulario.cleaned_data.get('username')
#             correo_u = formulario.cleaned_data.get('email')

#             subject = 'Registro en bienestar a la mano'
#             message = f'{username}, ¡Bienvenid@ a Bienestar a la mano!'
#             from_email = settings.EMAIL_HOST_USER
#             recipient_list = [correo_u]

#             send_mail(subject, message, from_email, recipient_list)
#             messages.success(request, "Registro exitoso. Hemos enviado un correo de bienvenida a tu dirección.")
#             return redirect('login')
#         return render(request, 'registration/registro.html', {'formulario':formulario,'auth_error': 'Autenticación fallida'})
#     else:
#         formulario = register()
#     return render(request, 'registration/registro.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        print(request.POST)
        formulario = register(request.POST)  # Asegúrate de que el formulario esté correctamente definido y llamado
        if formulario.is_valid():
            # Crear nuevo usuario sin guardar en la base de datos aún
            new_user = formulario.save(commit=False)
            new_user.set_password(formulario.cleaned_data['password'])  # Establecer la contraseña encriptada
            new_user.save()  # Guardar el usuario en la base de datos

            # Obtenemos el nombre de usuario y correo electrónico del formulario
            username = formulario.cleaned_data.get('username')
            correo_u = formulario.cleaned_data.get('email')

            # Preparar el correo electrónico de bienvenida
            subject = 'Registro en Bienestar a la Mano'
            message = f'{username}, ¡Bienvenid@ a Bienestar a la Mano!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [correo_u]

            # Enviar el correo electrónico
            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, "Registro exitoso. Hemos enviado un correo de bienvenida a tu dirección.")
            except Exception as e:
                # Manejar errores de envío de correo, como problemas de conexión SMTP
                messages.error(request, f"Registro exitoso, pero ocurrió un problema al enviar el correo de bienvenida: {e}")

            return redirect('login')  # Redirigir a la página de inicio de sesión después del registro
        else:
            # Manejo de formulario inválido
            return render(request, 'registration/registro.html', {'formulario': formulario, 'auth_error': 'Autenticación fallida'})
    else:
        formulario = register()  # Crear un formulario vacío para GET request
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
