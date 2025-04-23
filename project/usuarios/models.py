from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_image(file):
    max_size_kb = 5120  # Tamaño máximo en KB (5 MB)
    if file.size > max_size_kb * 1024:
        raise ValidationError("El tamaño máximo de la imagen es de 5 MB")
    if not file.content_type.startswith('image/'):
        raise ValidationError("El archivo debe ser una imagen")

class Usuario(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=50, unique=True)
    foto = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return f'{self.username}, {self.apellido}'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

