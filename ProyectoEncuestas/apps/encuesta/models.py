
# Create your models here.

 # This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Departamento(models.Model):
    iddepartamento = models.AutoField(db_column='IDDEPARTAMENTO', primary_key=True)  # Field name made lowercase.
    nombredepartamento = models.CharField(db_column='NOMBREDEPARTAMENTO', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEPARTAMENTO'


class Estacompuesto(models.Model):
    idpregunta = models.ForeignKey('Respuesta', models.DO_NOTHING, db_column='IDPREGUNTA', primary_key=True)  # Field name made lowercase.
    idreclamo = models.ForeignKey('Reclamo', models.DO_NOTHING, db_column='IDRECLAMO')  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTACOMPUESTO'
        unique_together = (('idpregunta', 'idreclamo'),)


class Municipio(models.Model):
    idmunicipio = models.AutoField(db_column='IDMUNICIPIO', primary_key=True)  # Field name made lowercase.
    iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='IDDEPARTAMENTO')  # Field name made lowercase.
    nombremunicipio = models.CharField(db_column='NOMBREMUNICIPIO', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MUNICIPIO'


class Reclamo(models.Model):
    idreclamo = models.AutoField(db_column='IDRECLAMO', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECLAMO'


class Respuesta(models.Model):
    idrespuesta = models.AutoField(db_column='IDRESPUESTA', primary_key=True)  # Field name made lowercase.
    numerodepregunta = models.IntegerField(db_column='NUMERODEPREGUNTA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESPUESTA'


class Tipotrasporte(models.Model):
    idtrasporte = models.AutoField(db_column='IDTRASPORTE', primary_key=True)  # Field name made lowercase.
    iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='IDDEPARTAMENTO', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOTRASPORTE'


class Usuario(models.Model):
    dui = models.CharField(db_column='DUI', primary_key=True, max_length=11)  # Field name made lowercase.
    idtrasporte = models.ForeignKey(Tipotrasporte, models.DO_NOTHING, db_column='IDTRASPORTE')  # Field name made lowercase.
    idreclamo = models.ForeignKey(Reclamo, models.DO_NOTHING, db_column='IDRECLAMO')  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=60)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=50)  # Field name made lowercase.
    edad = models.IntegerField(db_column='EDAD')  # Field name made lowercase.
    sexo = models.CharField(db_column='SEXO', max_length=6)  # Field name made lowercase.
    domicilio = models.TextField(db_column='DOMICILIO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO'

