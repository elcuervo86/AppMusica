from django.urls import path
from AppMusica import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    #path('vinilos', views.vinilos, name="Vinilos"),
    #path('cds', views.cds, name="CDs"),
    #path('clientes', views.clientes, name="Clientes"),
    #path('leerCliente', views.leerClientes, name = "LeerClientes"),
    #path('leerCd', views.leerCds, name = "LeerCds"),
    #path('leerVinilo', views.leerVinilos, name = "LeerVinilos"),
    #path('buscarCliente/', views.buscarCliente)

]
