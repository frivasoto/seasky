# Generated by Django 5.0.4 on 2024-05-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0029_transporte_remove_contenedor_otros_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenedor',
            name='hbl',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]