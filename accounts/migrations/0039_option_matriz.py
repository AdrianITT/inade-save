# Generated by Django 5.1 on 2024-12-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_remove_matriz_name_matriz_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='option_matriz',
            fields=[
                ('id_option_matriz', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False, unique=True)),
                ('s_option', models.IntegerField()),
            ],
        ),
    ]
