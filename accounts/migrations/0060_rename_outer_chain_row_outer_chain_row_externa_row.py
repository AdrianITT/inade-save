# Generated by Django 5.1 on 2025-01-06 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_remove_outer_chain_row_id_inforclient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outer_chain_row',
            old_name='outer_chain_row',
            new_name='externa_row',
        ),
    ]
