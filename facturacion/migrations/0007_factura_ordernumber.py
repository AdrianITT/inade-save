# Generated by Django 5.1 on 2024-09-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0006_factura_cfdisign_factura_originalstring_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='OrderNumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]