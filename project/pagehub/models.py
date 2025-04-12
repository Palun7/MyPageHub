from django.db import models

class SubCategoria(models.Model):
    sub_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_categoria

    class Meta:
        verbose_name = 'sub_categoría'
        verbose_name_plural = 'sub_categorías'

class PageHub(models.Model):
    class CategoriaPrincipal(models.TextChoices):
        ROPA = 'Ropa'
        HOGAR_DECO = 'Hogar/Deco'
        ACCESORIOS = 'Accesorios'
        RECETAS = 'Recetas'
        TECNOLOGIA = 'Tecnología'
        LIBROS = 'Libros'
        PLANTAS = 'Plantas'
        FOTOGRAFIA = 'Fotografía'
        ACADEMICO = 'Académico'

    categoria_principal = models.CharField(max_length=20, choices=CategoriaPrincipal.choices)
    sub_categoria = models.ManyToManyField(SubCategoria)
    nombre = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img', null=True, blank=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pagehub'
        verbose_name_plural = 'Pageshub'
