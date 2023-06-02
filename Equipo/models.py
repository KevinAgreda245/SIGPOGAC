from django.db import models

# Modelo de la tabla "tipo_equipo"
class TipoEquipo(models.Model):
    SK_TIPO_EQUIPO = models.AutoField(primary_key=True)
    ST_TIPO_EQUIPO = models.CharField(max_length=50, null=False,unique=True)

    class Meta:
        db_table = "tipo_equipo"

# Modelo de la tabla "equipo"
class Equipo(models.Model):
    SK_EQUIPO = models.AutoField(primary_key=True)
    ST_NOMBRE_EQUIPO = models.CharField(max_length=50,null=False,unique=True)
    ST_DESCRIPCION_EQUIPO = models.CharField(max_length=120,null=False)
    BN_ESTADO_EQUIPO = models.BooleanField(null=False,default=1)
    SK_TIPO_EQUIPO = models.ForeignKey(TipoEquipo,models.CASCADE)

    class Meta:
        db_table = "equipo"
