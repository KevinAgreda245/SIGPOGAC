# Generated by Django 4.0.1 on 2023-06-02 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='BN_ESTADO_EQUIPO',
            field=models.BooleanField(default=1),
        ),
    ]