# Generated by Django 5.1 on 2024-12-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_rename_contenedores_contenedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenedor',
            name='letra_contenedor',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
