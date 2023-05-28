from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Modelo de la tabla "usuario"
class Usuario(AbstractUser):
    ST_DUI_USUARIO = models.CharField(max_length=10,null=False,blank=False,unique=True)
    ST_NIT_USUARIO = models.CharField(max_length=17,null=True,blank=True,unique=True)
    ST_AFP_USUARIO = models.CharField(max_length=12,null=True,blank=True,unique=True)
    ST_ISSS_USUARIO = models.CharField(max_length=9,null=True,blank=True)
    FC_NACIMIENTO = models.DateField(null=False,blank=True)
    FC_INGRESO_USUARIO = models.DateTimeField(default=timezone.now)
    
    class Meta:
        db_table = "usuario"

# Modelo de la tabla "usuario_documento"
class DocumentoUsuario(models.Model):
    SK_DOC_USUARIO = models.AutoField(primary_key=True)
    ST_DOC_USUARIO = models.FileField(upload_to='doc_usuario/',null=False,blank=False)
    SK_USUARIO = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False,blank=False)

    class Meta:
        db_table = "usuario_documento"

