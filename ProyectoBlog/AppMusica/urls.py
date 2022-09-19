from django.urls import path
from AppMusica import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('acerca/', views.acercademi, name='acerca'), 
    path('rock', views.blogRock, name="Rock"),
    path('metal', views.blogMetal, name="Metal"),
    path('login', views.login_request, name='Login'),
    path('registro', views.registro, name="Registro"),
    path('logout', views.logout, name="Logout"),
    #path('clientes', views.clientes, name="Clientes"),
    #path('leerCliente', views.leerClientes, name = "LeerClientes"),
    #path('leerCd', views.leerCds, name = "LeerCds"),
    #path('leerVinilo', views.leerVinilos, name = "LeerVinilos"),
    #path('buscarCliente/', views.buscarCliente)

]
