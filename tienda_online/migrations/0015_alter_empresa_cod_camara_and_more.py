# Generated by Django 5.0.4 on 2024-04-30 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0014_alter_empresa_cod_camara_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cod_camara',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre_encargado',
            field=models.CharField(max_length=30),
        ),
    ]