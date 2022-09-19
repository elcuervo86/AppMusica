from distutils.text_file import TextFile
from django.db import models
from wsgiref.handlers import format_date_time
import datetime
from django.contrib.auth.models import User

# Create your models here.


class BlogRock(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField(max_length=5000)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.TextField()
    autor = models.CharField(max_length=200)

class BlogMetal(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.SlugField(max_length=200)
    cuerpo = models.TextField(max_length=5000)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.TextField()
    autor = models.CharField(max_length=200)

class Comentario(models.Model):
    nombre=models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    contenido=models.CharField(max_length=1200,null = False)
    fecha=models.DateTimeField(auto_now_add=True)


