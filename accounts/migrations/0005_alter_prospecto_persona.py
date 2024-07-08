# Generated by Django 5.0.6 on 2024-07-04 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_formato_avisos_formato_terminos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospecto',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prospecto', to='accounts.persona'),
        ),
    ]