# Generated by Django 5.1 on 2024-09-20 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_customuser_organizacion'),
        ('facturacion', '0003_remove_factura_almacen_remove_factura_sucursal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='sucursal',
            name='organizacion',
        ),
        migrations.DeleteModel(
            name='Almacen',
        ),
        migrations.DeleteModel(
            name='Sucursal',
        ),
    ]