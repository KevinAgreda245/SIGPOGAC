from datetime import datetime

from django.core.validators import FileExtensionValidator
from django.db import models


# Modelo de la tabla "tipo_equipo"
class TipoEquipo(models.Model):
    SK_TIPO_EQUIPO = models.AutoField(primary_key=True)
    ST_TIPO_EQUIPO = models.CharField(max_length=50, null=False, unique=True)

    class Meta:
        db_table = "tipo_equipo"

    def __str__(self):
        return self.ST_TIPO_EQUIPO


# Modelo de la tabla "equipo"
class Equipo(models.Model):
    SK_EQUIPO = models.AutoField(primary_key=True)
    ST_NOMBRE_EQUIPO = models.CharField(max_length=50, null=False, unique=True, verbose_name="Nombre")
    ST_DESCRIPCION_EQUIPO = models.CharField(max_length=120, null=False, verbose_name="Descripcion")
    BN_ESTADO_EQUIPO = models.BooleanField(null=False, default=1)
    FC_INGRESO = models.DateField(null=False, blank=True, verbose_name="Fecha de ingreso", default=datetime.now)
    ST_IMG_EQUIPO = models.FileField(upload_to='img_equipo/', null=False, blank=False, default='img_equipo/default.jpg', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], verbose_name="Imagen del equipo")
    SK_TIPO_EQUIPO = models.ForeignKey(TipoEquipo, models.CASCADE, verbose_name="Tipo de Equipo")

    class Meta:
        db_table = "equipo"