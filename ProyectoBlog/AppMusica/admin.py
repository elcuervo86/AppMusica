from django.contrib import admin

from AppMusica.models import BlogMetal, BlogRock, Comentario

# Register your models here.

admin.site.register(BlogRock)
admin.site.register(BlogMetal)
admin.site.register(Comentario)
#admin.site.register(Perfil)