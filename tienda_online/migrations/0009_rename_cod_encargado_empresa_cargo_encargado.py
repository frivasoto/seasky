# Generated by Django 5.0.4 on 2024-04-24 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0008_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='cod_encargado',
            new_name='cargo_encargado',
        ),
    ]
