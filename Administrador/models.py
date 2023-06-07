from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Modelo de la tabla "usuario"
class Usuario(AbstractUser):
    ST_DUI_USUARIO = models.CharField(max_length=10,null=False,blank=False,unique=True, verbose_name="DUI",error_messages={'unique': "Ya existe este DUI en el sistema."})
    ST_NIT_USUARIO = models.CharField(max_length=17,null=True,blank=True,unique=True, verbose_name="NIT")
    ST_AFP_USUARIO = models.CharField(max_length=12,null=True,blank=True,unique=True, verbose_name="AFP")
    ST_ISSS_USUARIO = models.CharField(max_length=9,null=True,blank=True, verbose_name="ISSS")
    FC_NACIMIENTO = models.DateField(null=False,blank=True, verbose_name="Fecha de nacimiento")
    FC_INGRESO_USUARIO = models.DateTimeField(default=timezone.now)
    
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

