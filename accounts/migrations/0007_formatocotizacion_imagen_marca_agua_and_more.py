# Generated by Django 5.1 on 2024-08-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_organizacion_logo_organizacion_slogan'),
    ]

    operations = [
        migrations.AddField(
            model_name='formatocotizacion',
            name='imagen_marca_agua',
            field=models.ImageField(blank=True, null=True, upload_to='marca_agua/'),
        ),
        migrations.AddField(
            model_name='formatocotizacion',
            name='mensaje_propuesta',
            field=models.TextField(blank=True, default='Gracias por la oportunidad de presentar nuestra propuesta. Por favor revise que se cumple con sus requerimientos; en caso contrario, comuníquese con nosotros.'),
        ),
        migrations.AddField(
            model_name='formatocotizacion',
            name='titulo_documento',
            field=models.CharField(blank=True, default='COTIZACIÓN / CONTRATO', max_length=255),
        ),
        migrations.AddField(
            model_name='formatoorden',
            name='imagen_marca_agua',
            field=models.ImageField(blank=True, null=True, upload_to='marca_agua/'),
        ),
        migrations.AddField(
            model_name='formatoorden',
            name='titulo_documento',
            field=models.CharField(blank=True, default='Orden de Trabajo', max_length=255),
        ),
    ]