from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')

class RestaForm(forms.Form):
    password = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    confirmar_password = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)