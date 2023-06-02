# Generated by Django 4.0.1 on 2023-06-02 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='FC_NACIMIENTO',
            field=models.DateField(blank=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ST_AFP_USUARIO',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='AFP'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ST_DUI_USUARIO',
            field=models.CharField(max_length=10, unique=True, verbose_name='DUI'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ST_ISSS_USUARIO',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='ISSS'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ST_NIT_USUARIO',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True, verbose_name='NIT'),
        ),
    ]
