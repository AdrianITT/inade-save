# Generated by Django 5.1 on 2024-10-15 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_notificacion_enlace'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacion',
            name='configuracion_sistema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizaciones', to='accounts.configuracionsistema'),
        ),
    ]