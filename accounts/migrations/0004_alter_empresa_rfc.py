# Generated by Django 5.0.7 on 2024-08-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_notificacion_usuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="rfc",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]