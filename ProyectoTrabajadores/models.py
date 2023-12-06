# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Cargas(models.Model):
    rut_carga = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    genero = models.CharField(max_length=9, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        managed = False
        db_table = 'cargas'


class Contactos(models.Model):
    rut_contacto = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.IntegerField(max_length=10, blank=False, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        managed = False
        db_table = 'contactos'

class Trabajadores(models.Model):
    rut_trabajador = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    departamento = models.CharField(max_length=25, blank=False, null=False)
    cargo = models.CharField(max_length=25, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.IntegerField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    contactos = models.ManyToManyField(Contactos, through="ListaContactos", blank=True)
    cargas = models.ManyToManyField(Cargas, through="ListaCargas", blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        managed = False
        db_table = 'trabajadores'

class ListaCargas(models.Model):
    id_lista_cargas = models.AutoField(primary_key=True)
    rut_trabajador = models.ForeignKey('Trabajadores', models.DO_NOTHING, db_column='rut_trabajador', blank=False, null=False)
    rut_carga = models.ForeignKey(Cargas, models.DO_NOTHING, db_column='rut_carga', blank=False, null=False)
    parentesco = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'lista_cargas'


class ListaContactos(models.Model):
    id_lista_contactos = models.AutoField(primary_key=True)
    rut_trabajador = models.ForeignKey('Trabajadores', models.DO_NOTHING, db_column='rut_trabajador', blank=False, null=False)
    rut_contacto = models.ForeignKey(Contactos, models.DO_NOTHING, db_column='rut_contacto', blank=False, null=False)
    relacion = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'lista_contactos'

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=25, blank=False, null=False)
    permisos = models.CharField(max_length=25, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'usuarios'