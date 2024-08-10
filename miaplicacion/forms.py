from django import forms

from django.contrib.auth.models import User

class Loginform(forms.Form): 
    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)

class register(forms.ModelForm):
    password = forms.CharField(label='password' ,widget=forms.PasswordInput)
    
    class Meta: 
        model = User
        fields = ['username', 'first_name', 'email']
