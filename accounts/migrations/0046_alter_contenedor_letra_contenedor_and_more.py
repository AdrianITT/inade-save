# Generated by Django 5.1 on 2024-12-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_alter_outer_chain_row_datetime_muestreo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenedor',
            name='letra_contenedor',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='contenedor',
            name='name_contenedor',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]