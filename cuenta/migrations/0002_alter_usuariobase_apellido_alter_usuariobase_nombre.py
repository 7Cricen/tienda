# Generated by Django 4.1.3 on 2022-12-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariobase',
            name='apellido',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='usuariobase',
            name='nombre',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
