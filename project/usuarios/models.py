from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return f'{self.username}, {self.apellido}'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

