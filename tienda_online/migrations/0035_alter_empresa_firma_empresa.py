# Generated by Django 5.0.4 on 2024-05-24 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0034_empresa_firma_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='firma_empresa',
            field=models.ImageField(blank=True, null=True, upload_to='firma_empresa/'),
        ),
    ]
