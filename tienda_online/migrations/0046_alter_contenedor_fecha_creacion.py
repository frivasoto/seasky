# Generated by Django 5.0.7 on 2024-07-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0045_alter_contenedor_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenedor',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
