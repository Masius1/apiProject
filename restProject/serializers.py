from rest_framework import serializers
from core.models import Asistencia, Alumno
from rest_framework import serializers
from django.contrib.auth.models import User


class AlumnoSerializer (serializers.ModelSerializer):
    class Meta:
        model= Alumno
        fields = ['id_alumno', 'rut', 'usuario', 'contrasena']


class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'rut_alumno', 'codigo_asignatura', 'nombre_asignatura', 'fecha', 'seccion', 'sede', 'escuela', 'docente']

class UpdateAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['id_asistencia', 'rut_alumno', 'codigo_asignatura', 'nombre_asignatura', 'fecha', 'seccion', 'sede', 'escuela', 'docente']

class UpdateAlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id_alumno', 'rut', 'usuario', 'contrasena']
        
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)        