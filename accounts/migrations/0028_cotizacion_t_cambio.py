# Generated by Django 5.1 on 2024-10-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_alter_configuracionsistema_tipo_de_cambio_dolar'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='t_cambio',
            field=models.CharField(choices=[('0.08', '8%'), ('0.16', '16%')], default=22.21, max_length=4),
            preserve_default=False,
        ),
    ]
