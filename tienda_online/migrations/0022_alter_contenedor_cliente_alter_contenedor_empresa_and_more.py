# Generated by Django 5.0.4 on 2024-05-02 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0021_alter_cliente_nombre_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenedor',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_online.cliente'),
        ),
        migrations.AlterField(
            model_name='contenedor',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_online.empresa'),
        ),
        migrations.AlterField(
            model_name='contenedor',
            name='importadora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_online.importadora'),
        ),
        migrations.AlterField(
            model_name='contenedor',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_online.proveedor'),
        ),
        migrations.AlterField(
            model_name='contenedor',
            name='puerto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_online.puerto'),
        ),
    ]
