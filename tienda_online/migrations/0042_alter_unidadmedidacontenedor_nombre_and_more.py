# Generated by Django 5.0.7 on 2024-07-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0041_remove_contenedor_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadmedidacontenedor',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unidadmedidacontenedor',
            name='sigla',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
