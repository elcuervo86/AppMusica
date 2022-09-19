from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppMusica.forms import BlogRockForm, BlogMetalForm, UserRegisterForm, UserEditForm
from AppMusica.models import BlogRock, BlogMetal, User, Comentario

# Create your views here.

def inicio(request):
      return render(request, 'inicio.html')

def acercademi(request):
      return render(request, "AppMusica/acercademi.html")

# Vistas Blog Rock
def blogRock(request):

      if request.method == "POST":

            miFormulario = BlogRockForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  blogRock = BlogRock(titulo=informacion['Titulo'], subtitulo=informacion['Subtitulo'], cuerpo=informacion['Cuerpo'], fecha=informacion['Fecha'], imagen=informacion['Imagen'], autor=informacion['Autor'])
                  blogRock.save()
                  return render(request, "AppMusica/inicio.html")
      else:
            miFormulario = BlogRockForm()

      return render(request, "AppMusica/rock.html", {"miFormulario": miFormulario})

def leer_blogRock(request):
      postsRock = BlogRock.objects.all() #trae todos los posts de Rock
      contexto= {"Posts":postsRock} 
      return render(request, "AppMusica/rock.html",contexto)

# Vistas Blog Metal
def blogMetal(request):

      if request.method == "POST":

            miFormulario = BlogMetalForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  blogMetal = BlogMetal(titulo=informacion['Titulo'], subtitulo=informacion['Subtitulo'], cuerpo=informacion['Cuerpo'], fecha=informacion['Fecha'], imagen=informacion['Imagen'], autor=informacion['Autor'])
                  blogMetal.save()
                  return render(request, "AppMusica/inicio.html")
      else:
            miFormulario = BlogMetalForm()

      return render(request, "AppMusica/metal.html", {"miFormulario": miFormulario})

def leer_blogMetal(request):
      postsMetal = BlogMetal.objects.all() #trae todos los posts de Rock
      contexto= {"Posts":postsMetal} 
      return render(request, "AppMusica/metal.html",contexto)

#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppMusica/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppMusica/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppMusica/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppMusica/login.html", {'form':form})

#REGISTRO
def registro(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppMusica/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppMusica/registro.html" ,  {"form":form})

#LOGOUT
def logout(request):
      return render(request, "AppMusica/logout.html")