

from django.db import models

# Create your models here.
 
class Asistencia(models.Model):
    id_asistencia = models.IntegerField(primary_key=True, verbose_name='Id de asistencia')
    rut_alumno = models.CharField(max_length=15, verbose_name='rut del alumno')
    codigo_asignatura = models.CharField(max_length=20, verbose_name='Codigo de la asignatura')
    nombre_asignatura = models.CharField(max_length=50, verbose_name='Nombre asignatura')
    fecha = models.DateField(auto_now=True)
    seccion = models.CharField(max_length=20, verbose_name='seccion del alumno')
    sede = models.CharField(max_length=50, verbose_name='Sede del alumno')
    escuela = models.CharField(max_length=50, verbose_name='Escuela a la que pertence el alumno')
    docente = models.CharField(max_length=100, verbose_name='Nombre del docente a cargo')

    def _str_(self):
        return self.rut_alumno

class Alumno(models.Model):
    id_alumno = models.IntegerField(primary_key=True, verbose_name='id de alumno')
    rut = models.CharField(max_length=15, verbose_name='rut del almuno')
    usuario = models.CharField(max_length=100, verbose_name='Nombre de usuario del alumno')
    contrasena = models.CharField(max_length=100, verbose_name='contraseña del alumno')

    def _str_(self):
        return self.rut