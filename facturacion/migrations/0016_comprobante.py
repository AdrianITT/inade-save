# Generated by Django 5.1 on 2024-10-04 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0015_alter_factura_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('folio', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cfdi_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('ref_cfdi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facturacion.factura')),
            ],
        ),
    ]
