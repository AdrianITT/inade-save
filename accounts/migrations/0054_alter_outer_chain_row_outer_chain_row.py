# Generated by Django 5.1 on 2024-12-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_outer_chain_row_identificador_campo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outer_chain_row',
            name='outer_chain_row',
            field=models.AutoField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
