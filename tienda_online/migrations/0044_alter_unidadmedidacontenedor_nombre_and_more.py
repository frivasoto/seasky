# Generated by Django 5.0.7 on 2024-07-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0043_contenedor_unidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadmedidacontenedor',
            name='nombre',
            field=models.CharField(blank=True, default='Libras', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='unidadmedidacontenedor',
            name='sigla',
            field=models.CharField(blank=True, default='LB', max_length=5, null=True),
        ),
    ]
