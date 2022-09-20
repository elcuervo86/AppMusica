from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppMusica.forms import BlogRockForm, BlogMetalForm, ComentarioForm, UserRegisterForm, UserEditForm
from AppMusica.models import BlogRock, BlogMetal, Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
      return render(request, 'inicio.html')

def acercademi(request):
      return render(request, "AppMusica/acercademi.html")



# Vistas Blog Rock
@login_required
def blogRock(request):

      if request.method == "POST":

            miFormulario = BlogRockForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  blogRock = BlogRock(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo=informacion['cuerpo'], imagen=informacion['imagen'], autor=informacion['autor'])
                  blogRock.save()
                  return render(request, "AppMusica/inicio.html")
      else:
            miFormulario = BlogRockForm()

      return render(request, "AppMusica/rock.html", {"miFormulario": miFormulario})

@login_required
def leer_blogRock(request):
      postsRock = BlogRock.objects.all() #trae todos los posts de Rock
      contexto= {"PostsRock":postsRock} 
      return render(request, "AppMusica/rock.html",contexto)


# Vistas Blog Metal
@login_required
def blogMetal(request):

      if request.method == "POST":

            miFormulario = BlogMetalForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  blogMetal = BlogMetal(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo=informacion['cuerpo'], imagen=informacion['imagen'], autor=informacion['autor'])
                  blogMetal.save()
                  return render(request, "AppMusica/inicio.html")
      else:
            miFormulario = BlogMetalForm()

      return render(request, "AppMusica/metal.html", {"miFormulario": miFormulario})

@login_required
def leer_blogMetal(request):
      postsMetal = BlogMetal.objects.all() #trae todos los posts de Rock
      contexto= {"Posts":postsMetal} 
      return render(request, "AppMusica/metal.html",contexto)

@login_required
def comentario(request):

      if request.method == "POST":

            miFormulario = ComentarioForm(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  comentario = Comentario(nombre=informacion['Nombre'], contenido=informacion['Contenido'], fecha=informacion['Fecha'])
                  comentario.save()
                  return render(request, "AppMusica/inicio.html")
      else:
            miFormulario = ComentarioForm()

      return render(request, "AppMusica/comentario.html", {"miFormulario": miFormulario})

#Para el login

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppMusica/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppMusica/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppMusica/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"AppMusica/login.html", {'form':form})

#REGISTRO
def registro(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppMusica/inicio.html" ,  {"mensaje":"Usuario Creado con Exito"})

      else:       
            form = UserRegisterForm()     

      return render(request,"AppMusica/registro.html" ,  {"form":form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "AppMusica/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppMusica/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

#LOGOUT
def logout(request):
      return render(request, "AppMusica/logout.html")


