from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from wsgiref.handlers import format_date_time


class BlogRockForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    cuerpo = forms.CharField(max_length=5000)
    fecha = forms.DateField()
    imagen = forms.TextInput()
    autor = forms.CharField(max_length=200)


class BlogMetalForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    cuerpo = forms.CharField(max_length=5000)
    fecha = forms.DateField()
    imagen = forms.TextInput()
    autor = forms.CharField(max_length=200)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    nombre = forms.CharField(label="Ingrese su Apellido:")
    apellido = forms.CharField(label="Ingrese su Nombre:")
    edad= forms.IntegerField(label="Ingrese su Edad")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']