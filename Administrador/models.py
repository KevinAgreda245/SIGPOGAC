from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Modelo de la tabla "usuario"
class Usuario(AbstractUser):
    email = models.EmailField(unique=True,blank=False,verbose_name="Dirección de correo electrónico", error_messages={'unique': "El correo ingresado ya existe en el sistema. Por favor, ingrese otro correo."})
    ST_DUI_USUARIO = models.CharField(max_length=10,null=False,blank=False,unique=True, verbose_name="DUI",error_messages={'unique': "El DUI ingresado ya existe en el sistema. Por favor, ingrese otro DUI."})
    ST_NIT_USUARIO = models.CharField(max_length=17,null=True,blank=True,unique=True, verbose_name="NIT",error_messages={'unique': "El NIT ingresado ya existe en el sistema. Por favor, ingrese otro NIT."})
    ST_AFP_USUARIO = models.CharField(max_length=12,null=True,blank=True,unique=True, verbose_name="AFP")
    ST_ISSS_USUARIO = models.CharField(max_length=9,null=True,blank=True, verbose_name="ISSS")
    FC_NACIMIENTO = models.DateField(null=False,blank=True, verbose_name="Fecha de nacimiento")
    FC_INGRESO_USUARIO = models.DateTimeField(default=timezone.now)
    BN_ESTADO_USUARIO = models.BooleanField(null=False,default=1) 
    
    class Meta:
        db_table = "usuario"

# Modelo de la tabla "usuario_documento"
class DocumentoUsuario(models.Model):
    TIPO = [
        ('DUI','DUI'),
        ('NIT','NIT'),
        ('ISSS','ISSS'),
        ('AFP','AFP'),
    ]
    SK_DOC_USUARIO = models.AutoField(primary_key=True)
    ST_TIPO_DOC_USUARIO = models.CharField(max_length=50,choices=TIPO)
    ST_DOC_USUARIO = models.FileField(upload_to='doc_usuario/',null=False,blank=False)
    SK_USUARIO = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False,blank=False)

    class Meta:
        db_table = "usuario_documento"

