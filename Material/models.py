from django.db import models

class Material(models.Model):
    SK_MATERIAL = models.AutoField(primary_key=True)
    ST_NOMBRE_MATERIAL = models.CharField(max_length=60,null=False,unique=True)
    ST_DESCRIPCION_MATERIAL = models.CharField(max_length=120,null=False)
    BN_ESTADO_MATERIAL = models.BooleanField(null=False,default=1) 

    class Meta:
        db_table = "material"
