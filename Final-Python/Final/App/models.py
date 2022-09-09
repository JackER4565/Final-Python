from django.db import models

# Create your models here.
class Blog(models.Model):
    icono = models.CharField(max_length=50, default="fa-hand-point-right")
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto_corto = models.CharField(max_length=40)
    texto_largo = models.TextField()
    imagen = models.ImageField(upload_to='images/',verbose_name='Imagen', null=True, blank=True)
    autor = models.CharField(max_length=20)
    fecha = models.DateField(auto_now_add=True)
    activo = models.IntegerField() # 1 activa, 2 no activa
