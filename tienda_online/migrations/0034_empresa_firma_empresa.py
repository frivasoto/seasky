# Generated by Django 5.0.4 on 2024-05-24 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0033_alter_estado_options_proveedor_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='firma_empresa',
            field=models.ImageField(blank=True, null=True, upload_to='logo_empresa/'),
        ),
    ]
