# Generated by Django 5.1 on 2024-12-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_rename_id_unidad_medida_outer_chain_row_iunidad_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='outer_chain_row',
            name='identificador_campo',
            field=models.CharField(default='null', max_length=10),
        ),
    ]