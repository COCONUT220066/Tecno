from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):
    class Meta: 
        model = Usuario
        fields = ['correo_u','idusuario','nombre','contacto','ficha','contraseña']

class CustomUserCreationForm(UserCreationForm):
    pass        
