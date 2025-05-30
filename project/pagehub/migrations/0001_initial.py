# Generated by Django 5.1.7 on 2025-03-24 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_categoria', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'sub_categoría',
                'verbose_name_plural': 'sub_categorías',
            },
        ),
        migrations.CreateModel(
            name='PageHub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_principal', models.CharField(choices=[('Ropa', 'Ropa'), ('Hogar y Deco', 'Hogar Deco'), ('Accesorios', 'Accesorios'), ('Recetas', 'Recetas'), ('Tecnología', 'Tecnologia'), ('Libros', 'Libros'), ('Plantas', 'Plantas'), ('Fotografía', 'Fotografia'), ('Académico', 'Academico')], max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img')),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('sub_categoria', models.ManyToManyField(to='pagehub.subcategoria')),
            ],
        ),
    ]
