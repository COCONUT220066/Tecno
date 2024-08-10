
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django import forms
from django.contrib import messages
from .models import AuthUser
from .tokens import custom_token_generator
from .functions import send_mail_google, refresh_google_token
from django.contrib.auth.hashers import make_password



# Vistas

class EmailForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico')

class EnviarMensaje(FormView):
    template_name = 'enviar.html'
    form_class = EmailForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = AuthUser.objects.get(email=email)
        except AuthUser.DoesNotExist:
            messages.error(self.request, 'Correo electrónico no encontrado.')
            return self.form_invalid(form)

        # Intenta actualizar el token de Google
        refresh_google_token()

        token = custom_token_generator.make_token(user)
        reset_url = self.request.build_absolute_uri(reverse('resta', kwargs={
            'username': user.username,
            'token': token,
        }))
        message_text = f'Para restablecer tu contraseña haz clic en el siguiente enlace: {reset_url}'

        sent = send_mail_google(email, 'Restablecer contraseña', message_text)
        if sent:
            messages.success(self.request)
        else:
            messages.error(self.request, 'Error al enviar el correo. Inténtalo de nuevo más tarde.')
        return super().form_valid(form)


def resta(request, username, token):
    usuario = get_object_or_404(AuthUser, username=username)

    if not custom_token_generator.check_token(usuario, token):
        messages.error(request, 'El enlace de restablecimiento no es válido o ha expirado.')
        return redirect('password_reset')

    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            # Usar el método corregido para cifrar la contraseña
            usuario.actualizar_contrasenia(password)
            messages.success(request, 'Restablecimiento Exitoso')
            return redirect('login')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'resta.html', {'username': username, 'token': token})

    return render(request, 'resta.html', {'username': username, 'token': token})
