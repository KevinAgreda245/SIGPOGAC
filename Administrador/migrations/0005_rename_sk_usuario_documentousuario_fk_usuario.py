# Generated by Django 4.0.1 on 2023-06-11 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0004_alter_usuario_st_afp_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentousuario',
            old_name='SK_USUARIO',
            new_name='FK_USUARIO',
        ),
    ]
