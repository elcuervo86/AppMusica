from django.urls import path
from AppMusica import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('acerca', views.acercademi, name='acerca'), 
    path('rock', views.blogRock, name="Rock"),
    path('metal', views.blogMetal, name="Metal"),
    path('login', views.login_request, name='Login'),
    path('registro', views.registro, name="Registro"),
    path('logout', LogoutView.as_view(template_name='AppMusica/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name = "EditarPerfil"),
    path('leerBlockRock', views.leerBlogRock, name = "LeerBlogRock"),
    path('eliminarBlockRock', views.eliminarBlogRock, name = "EliminarBlogRock"),
    #path('leerVinilo', views.leerVinilos, name = "LeerVinilos"),
    #path('buscarCliente/', views.buscarCliente)

]
