from msilib.schema import Class
from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppMusica.forms import BlogRockForm, BlogMetalForm, ComentarioForm, UserRegisterForm, UserEditForm
from AppMusica.models import BlogRock, BlogMetal, Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class BlogRockList(ListView):
      model = BlogRock
      template_name: "AppMusica/blogrock_list.html"

class BlogRockDetalle(DetailView):
    model = BlogRock
    template_name = "AppMusica/blogrock_detalle.html"

class BlogRockCreacion(CreateView):
    model = BlogRock
    success_url = "/AppMusica/rock/list"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']

class BlogRockUpdate(UpdateView):
    model = BlogRock
    success_url = "/AppMusica/rock/list"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']

class BlogRockDelete(DeleteView):
    model = BlogRock
    success_url = "/AppMusica/rock/list"

# Vistas Blog Metal
@login_required
def blogMetal(request):

      if request.method == "POST":

            miFormulario = BlogMetalForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  blogMetal = BlogMetal (titulo=informacion['Titulo'], subtitulo=informacion['Subtitulo'], cuerpo=informacion['Cuerpo'], imagen=informacion['Imagen'], autor=informacion['Autor'])
                  blogMetal.save()
                  return render(request, "AppMusica/inicio.html")
      else:
            miFormulario = BlogMetalForm()

      return render(request, "AppMusica/metal.html", {"miFormulario": miFormulario})


class BlogMetalList(ListView):
      model = BlogMetal
      template_name: "AppMusica/blogmetal_list.html"

class BlogMetalDetalle(DetailView):
    model = BlogMetal
    template_name = "AppMusica/blogmetal_detalle.html"

class BlogMetalCreacion(CreateView):
    model = BlogMetal
    success_url = "/AppMusica/metal/list"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']

class BlogMetalUpdate(UpdateView):
    model = BlogMetal
    success_url = "/AppMusica/metal/list"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']

class BlogMetalDelete(DeleteView):
    model = BlogMetal
    success_url = "/AppMusica/metal/list"

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

class ComentarioList(ListView):
      model = Comentario
      template_name: "AppMusica/comentario_list.html"

class ComentarioDetalle(DetailView):
    model = Comentario
    template_name = "AppMusica/comentario_detalle.html"

class ComentarioCreacion(CreateView):
    model = Comentario
    success_url = "/AppMusica/comentario/list"
    fields = ['nombre', 'contenido']

class ComentarioUpdate(UpdateView):
    model = Comentario
    success_url = "/AppMusica/comentario/list"
    fields = ['nombre', 'contenido']

class ComentarioDelete(DeleteView):
    model = Comentario
    success_url = "/AppMusica/comentario/list"


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


