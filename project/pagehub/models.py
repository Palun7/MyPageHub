from django.db import models
from usuarios.models import User

class CategoriaPrincipal(models.Model):
    nombre = models.CharField(max_length=50, unique=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Categoría Principal'
        verbose_name_plural = 'Categorías Principales'

class PageHub(models.Model):

    categoria_principal = models.ForeignKey(CategoriaPrincipal, on_delete=models.CASCADE, null=True, blank=True, default=None)
    sub_categoria = models.ForeignKey('SubCategoria', on_delete=models.CASCADE, null=True, blank=True, default=None)
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img', null=True, blank=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pagehub'
        verbose_name_plural = 'Pageshub'

class SubCategoria(models.Model):

    categoria_principal = models.ForeignKey(CategoriaPrincipal, on_delete=models.CASCADE, null=True, blank=True, default=None)
    sub_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_categoria

    class Meta:
        verbose_name = 'sub_categoría'
        verbose_name_plural = 'sub_categorías'