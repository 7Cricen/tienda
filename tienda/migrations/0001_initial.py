# Generated by Django 4.1.3 on 2022-12-09 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(default='admin', max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('imagen', models.ImageField(default='images/default.png', upload_to='images/')),
                ('slug', models.SlugField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('en_stock', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='tienda.categoria')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_creador', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'ordering': ('-creado',),
            },
        ),
    ]
