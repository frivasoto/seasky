# Generated by Django 5.0.4 on 2024-04-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='referencia',
            field=models.CharField(max_length=10),
        ),
    ]
