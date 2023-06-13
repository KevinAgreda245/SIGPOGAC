from django.db import models
from django.utils import timezone
from Administrador.models import Usuario

# Modelo de la tabla "cliente"
class Cliente(models.Model):
    SK_CLIENTE = models.AutoField(primary_key=True)
    ST_NOMBRE_CLIENTE = models.CharField(max_length=100,null=False,blank=False,unique=True,error_messages={'unique': "El nombre del cliente ingresado ya existe en el sistema. Por favor, ingrese otro nombre."})
    ST_DOC_CLIENTE = models.CharField(max_length=75,null=False,blank=False,unique=True,error_messages={'unique': "El documento del cliente ingresado ya existe en el sistema. Por favor, ingrese otro documento."})
    ST_NIT_CLIENTE = models.CharField(max_length=17,null=False,blank=False,unique=True,error_messages={'unique': "El NIT del cliente ingresado ya existe en el sistema. Por favor, ingrese otro NIT."})
    BN_TIPO_CLIENTE = models.BooleanField(null=False,blank=False)
    FK_USUARIO = models.ForeignKey(Usuario,models.CASCADE)
    FC_INGRESO_CLIENTE = models.DateTimeField(default=timezone.now)
    BN_ESTA_ACTIVO=models.BooleanField(null=False,blank=False,default=True)

    class Meta:
        db_table = "cliente"

