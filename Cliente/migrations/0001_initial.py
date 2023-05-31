# Generated by Django 4.0.1 on 2023-05-30 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('SK_CLIENTE', models.AutoField(primary_key=True, serialize=False)),
                ('ST_NOMBRE_CLIENTE', models.CharField(max_length=100, unique=True)),
                ('ST_DOC_CLIENTE', models.CharField(max_length=75, unique=True)),
                ('ST_NIT_CLIENTE', models.CharField(max_length=17, unique=True)),
                ('BN_TIPO_CLIENTE', models.BooleanField()),
                ('FC_INGRESO_CLIENTE', models.DateTimeField(default=django.utils.timezone.now)),
                ('SK_USUARIO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]
