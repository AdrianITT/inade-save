# Generated by Django 5.1 on 2024-09-17 21:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_empresa_regimen_fiscal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='usuario',
            field=models.ForeignKey(blank=True, max_length=10, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]