# Generated by Django 5.1 on 2024-08-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_queja_archivo_adjunto_queja_prioridad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rol',
            field=models.CharField(blank=True, choices=[('admin', 'Administrador'), ('coordinador', 'Coordinador'), ('muestras', 'Muestras'), ('informes', 'Informes'), ('laboratorio', 'Laboratorio'), ('calidad', 'Calidad')], default='admin', max_length=20, null=True),
        ),
    ]