from django.urls import path
from AppMusica import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

#from AppMusica.views import BlogMetalUpdate

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('acerca', views.acercademi, name='acerca'), 
    path('login', views.login_request, name='Login'),
    path('registro', views.registro, name="Registro"),
    path('logout', LogoutView.as_view(template_name='AppMusica/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name = "EditarPerfil"),
    path('comentario/list', login_required(views.ComentarioList.as_view()), name='List'),
    path(r'^(?P<pk>\d+)$', views.ComentarioDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ComentarioCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ComentarioUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ComentarioDelete.as_view(), name='Delete'),
    path('metal/list', login_required(views.BlogMetalList.as_view()), name='metalList'),
    path(r'^detailmetal(?P<pk>\d+)$', views.BlogMetalDetalle.as_view(), name='metalDetail'),
    path(r'^nuevometal$', views.BlogMetalCreacion.as_view(), name='metalNew'),
    path(r'^editarmetal/(?P<pk>\d+)$', views.BlogMetalUpdate.as_view(), name='metalEdit'),
    path(r'^borrarmetal/(?P<pk>\d+)$', views.BlogMetalDelete.as_view(), name='metalDelete'),
    path('rock/list', login_required(views.BlogRockList.as_view()), name='rockList'),
    path(r'^detailrock/(?P<pk>\d+)$', views.BlogRockDetalle.as_view(), name='rockDetail'),
    path(r'^nuevorock$', views.BlogRockCreacion.as_view(), name='rockNew'),
    path(r'^editarrock/(?P<pk>\d+)$', views.BlogRockUpdate.as_view(), name='rockEdit'),
    path(r'^borrarrock/(?P<pk>\d+)$', views.BlogRockDelete.as_view(), name='rockDelete'),

]
