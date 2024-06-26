# Generated by Django 5.0.4 on 2024-05-03 19:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0024_alter_llenarcontenedor_contenedor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contenedor',
            options={'ordering': ['fecha_creacion'], 'verbose_name': 'Contenedor', 'verbose_name_plural': 'Contenedores'},
        ),
        migrations.AddField(
            model_name='contenedor',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
