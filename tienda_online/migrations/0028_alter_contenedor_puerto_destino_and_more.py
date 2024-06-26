# Generated by Django 5.0.4 on 2024-05-10 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0027_remove_contenedor_puerto_contenedor_puerto_destino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenedor',
            name='puerto_destino',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='puerto_destino', to='tienda_online.puerto'),
        ),
        migrations.AlterField(
            model_name='contenedor',
            name='puerto_origen',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='puerto_origen', to='tienda_online.puerto'),
        ),
    ]
