# Generated by Django 5.0.4 on 2024-04-22 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0005_pais_puerto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pais',
            old_name='nombre',
            new_name='nombre_pais',
        ),
        migrations.RenameField(
            model_name='puerto',
            old_name='nombre',
            new_name='nombre_puerto',
        ),
    ]