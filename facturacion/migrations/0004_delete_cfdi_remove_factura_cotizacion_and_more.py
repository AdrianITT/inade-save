# Generated by Django 5.1 on 2024-09-20 22:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_remove_sucursal_direccion_and_more'),
        ('facturacion', '0003_remove_factura_almacen_remove_factura_sucursal'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CFDI',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='cotizacion',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='fecha_emision',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='pdf_factura',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='regimen_fiscal_receptor',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='rfc_receptor',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='xml_timbrado',
        ),
        migrations.AddField(
            model_name='factura',
            name='cfdi_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='accounts.persona'),
        ),
        migrations.AddField(
            model_name='factura',
            name='emisor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='accounts.organizacion'),
        ),
        migrations.AddField(
            model_name='factura',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='factura',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='factura',
            name='orden',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ordentrabajo'),
        ),
        migrations.AddField(
            model_name='factura',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='cfdis/pdf/'),
        ),
        migrations.AddField(
            model_name='factura',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='factura',
            name='xml_file',
            field=models.FileField(blank=True, null=True, upload_to='cfdis/xml/'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.CharField(default='Creada', max_length=20),
        ),
        migrations.AlterField(
            model_name='factura',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]