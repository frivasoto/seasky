# Generated by Django 5.0.4 on 2024-05-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0018_alter_producto_partida_arancelaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='partidaarancelaria',
            name='descripcion',
            field=models.TextField(default='None', max_length=500),
            preserve_default=False,
        ),
    ]