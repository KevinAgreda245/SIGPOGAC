from django.db import models
from django.utils import timezone
from Cliente.models import Cliente
from Administrador.models import Usuario
from Equipo.models import Equipo
from Material.models import Material

# Modelo de la tabla "tipo_servicio"
class TipoServicio(models.Model):
    SK_TIPO_SERVICIO = models.AutoField(primary_key=True)
    ST_TIPO_SERVICIO = models.CharField(max_length=75,null=False,blank=False)

    class Meta: 
        db_table = "tipo_servicio"

    def __str__(self):
        return self.ST_TIPO_SERVICIO

# Modelo de la tabla "estado_proyecto"
class EstadoProyecto(models.Model):
    SK_ESTADO_PROYECTO = models.AutoField(primary_key=True)
    ST_ESTADO_PROYECTO = models.CharField(max_length=75,null=False,blank=False)

    class Meta: 
        db_table = "estado_proyecto"
    
    def __str__(self):
        return self.ST_ESTADO_PROYECTO

# Modelo de la tabla "proyecto"
class Proyecto(models.Model):
    SK_PROYECTO = models.AutoField(primary_key=True)
    ST_DIRECCION_PROYECTO = models.CharField(max_length=120,null=False,blank=False,verbose_name="Dirección:")
    NM_LATITUD_PROYECTO = models.FloatField(null=False,blank=False)
    NM_LONGITUD_PROYECTO = models.FloatField(null=False,blank=False)
    ST_DESCRIPCION_PROYECTO = models.CharField(max_length=120,null=False,blank=False,verbose_name="Descripción:")
    FK_CLIENTE = models.ForeignKey(Cliente,models.CASCADE,verbose_name="Cliente")
    FK_ESTADO_PROYECTO = models.ForeignKey(EstadoProyecto,models.CASCADE,verbose_name="Estado:")
    FK_TIPO_SERVICIO = models.ForeignKey(TipoServicio,models.CASCADE,verbose_name="Tipo de Servicio:") 
    FK_USUARIO = models.ForeignKey(Usuario,models.CASCADE)
    FC_INGRESO_PROYECTO = models.DateTimeField(default=timezone.now)

    class Meta: 
        db_table = "proyecto"

# Modelo de la tabla "factura"
class Factura(models.Model):
    SK_FACTURA = models.AutoField(primary_key=True)
    ST_FACTURA = models.FileField(upload_to='factura/',null=False,blank=False)
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)

    class Meta: 
        db_table = "factura"

# Modelo de la tabla de "asignacion_empleado"
class AsignacionEmpleado(models.Model):
    SK_ASIG_EMPLEADO = models.AutoField(primary_key=True)
    SK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    FK_USUARIO = models.ForeignKey(Usuario,models.CASCADE)

    class Meta:
        db_table = "asignacion_empleado"

# Modelo de la tabla "asignacion_equipo"
class AsignacionEquipo(models.Model):
    SK_ASIG_EQUIPO = models.AutoField(primary_key=True)
    SK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    FK_EQUIPO = models.ForeignKey(Equipo,models.CASCADE)

    class Meta:
        db_table = "asignacion_equipo"

# Modelo de la tabla "asignacion_material"
class AsignacionMaterial(models.Model):
    SK_ASIG_MATERIAL = models.AutoField(primary_key=True)
    ST_DESCRIPCION = models.CharField(max_length=50,null=True,blank=True)
    SK_MATERIAL = models.ForeignKey(Material,models.CASCADE)
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    
    class Meta:
        db_table = "asignacion_material"
    
class Concreto(models.Model):
    TIPO_DOC = [
        ('PLANO','Plano'),
        ('ESPECIFICACIONES','Especificaciones')
    ]
    SK_CONCRETO = models.AutoField(primary_key=True)
    ST_TIPO_DOC_CONCRETO = models.CharField(max_length=25,choices=TIPO_DOC)
    ST_DOC_CONCRETO = models.FileField(upload_to='doc_concreto/',null=False,blank=False)
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)

    class Meta:
        db_table = "concreto"
    
class RentaEquipo(models.Model):
    SK_RENTA_EQUIPO = models.AutoField(primary_key=True)
    FC_SALIDA_EQUIPO = models.DateTimeField(null=False,blank=False)
    FC_ENTRADA_EQUIPO = models.DateTimeField(null=False,blank=False)
    ST_TIPO_USO = models.CharField(max_length=100,null=False,blank=False, verbose_name="Tipo de uso:")
    ST_OBSERVACION_EQUIPO = models.CharField(max_length=120, null=True,blank=False, verbose_name="Observación:") 
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    class Meta:
        db_table = "renta_equipo"

class RentaDesimetro(models.Model):
    SK_RENTA_DESIMETRO = models.AutoField(primary_key=True)
    FC_SALIDA_DESIMETRO = models.DateTimeField(null=False,blank=False)
    FC_ENTRADA_DESIMETRO = models.DateTimeField(null=False,blank=False)
    ST_NOMBRE_TECNICO = models.CharField(max_length=50,null=False,blank=False)
    ST_OBSERVACION_DESIMETRO = models.CharField(max_length=120, null=True,blank=False)
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    class Meta:
        db_table = "renta_desimetro"
        
class Transporte(models.Model):
    UNIDADES = [
        ('LITRO','Litro'),
        ('MILILITRO','Mililitro'),
        ('METRO_CUBICO','Metro cúbico'),
        ('PULGADA_CUBICA','Pulgada cúbica'),
        ('GALON','Galón')
    ]
    SK_TRANSPORTE = models.AutoField(primary_key=True)
    NM_VOLUMEN = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False, verbose_name="Volumen:")
    ST_UNIDAD_TRANSPORTE = models.CharField(max_length=50,choices=UNIDADES, verbose_name="Unidad de volumen:")
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    class Meta:
        db_table = "transporte"

class LevantamientoTopografico(models.Model):
    UNIDADES = [
        ('METRO_CUADRADRO','Metro cuadrado'),
        ('PULGADA_CUADRADA','Pulgada cuadrada'),
        ('PIE_CUADRADO','Pie cuadrado'),
        ('HECTAREA','Hectárea'),
        ('ACRE','Acre')
    ]
    SK_LEVANTAMIENTO_TOPOGRAFICO = models.AutoField(primary_key=True)
    NM_AREA = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False)
    ST_UNIDAD_LEVANTAMIENTO = models.CharField(max_length=50,choices=UNIDADES)
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    class Meta:
        db_table = "levantamiento_topografico"

class EstructuraMetalica(models.Model):
    TIPO_DOC = [
        ('PLANO','Plano'),
        ('ESPECIFICACIONES','Especificaciones')
    ]
    SK_ESTRUCTURA_METALICA = models.AutoField(primary_key=True)
    ST_TIPO_DOC_CONCRETO = models.CharField(max_length=25,choices=TIPO_DOC)
    ST_DOC_CONCRETO = models.FileField(upload_to='doc_vial/',null=False,blank=False)
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    class Meta:
        db_table = "estructura_metalica"

class SenializacionVial(models.Model):
    SK_SENIALIZACION_VIAL = models.AutoField(primary_key=True)
    ST_ESPECIFICACION_VIAL = models.CharField(max_length=120,null=False,blank=False)
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)
    class Meta:
        db_table = "senializacion_vial"

class AsesoriaConstructiva(models.Model):
    UNIDADES = [
        ('DIA','Día'),
        ('MES','Mes'),
        ('AÑO','Año')
    ]
    SK_ASESORIA = models.AutoField(primary_key=True)
    NM_TIEMPO = models.IntegerField(null=False,blank=False)
    ST_UNIDAD_ASESORIA = models.CharField(max_length=50,choices=UNIDADES)
    FK_PROYECTO = models.ForeignKey(Proyecto,models.CASCADE)

    class Meta:
        db_table = "asesoria_constructiva"