# Generated by Django 5.0.4 on 2024-04-30 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0015_alter_empresa_cod_camara_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadDeMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad_medida',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_online.unidaddemedida'),
        ),
    ]
