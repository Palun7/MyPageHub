from django.db import models
from usuarios.models import User

class SubCategoria(models.Model):
    class CategoriaPrincipal(models.TextChoices):
        ROPA = 'Ropa'
        HOGAR_DECO = 'Hogar-Deco'
        ACCESORIOS = 'Accesorios'
        RECETAS = 'Recetas'
        TECNOLOGIA = 'Tecnologia'
        LIBROS = 'Libros'
        PLANTAS = 'Plantas'
        FOTOGRAFIA = 'Fotografia'
        ACADEMICO = 'Academico'

    categoria_principal = models.CharField(max_length=20, choices=CategoriaPrincipal.choices, null=True, blank=True)
    sub_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_categoria

    class Meta:
        verbose_name = 'sub_categoría'
        verbose_name_plural = 'sub_categorías'

class PageHub(models.Model):
    class CategoriaPrincipal(models.TextChoices):
        ROPA = 'Ropa'
        HOGAR_DECO = 'Hogar-Deco'
        ACCESORIOS = 'Accesorios'
        RECETAS = 'Recetas'
        TECNOLOGIA = 'Tecnologia'
        LIBROS = 'Libros'
        PLANTAS = 'Plantas'
        FOTOGRAFIA = 'Fotografia'
        ACADEMICO = 'Academico'

    categoria_principal = models.CharField(max_length=20, choices=CategoriaPrincipal.choices)
    sub_categoria = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img', null=True, blank=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    user = models.ForeignKey(User, auto_created=True, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pagehub'
        verbose_name_plural = 'Pageshub'
