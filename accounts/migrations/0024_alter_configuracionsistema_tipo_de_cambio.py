# Generated by Django 5.1 on 2024-10-15 21:26

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_configuracionsistema_tipo_de_cambio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracionsistema',
            name='tipo_de_cambio',
            field=models.DecimalField(decimal_places=2, default=Decimal('18.00'), max_digits=5),
        ),
    ]
