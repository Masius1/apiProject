from http.client import OK
import json
from pickle import FALSE, PUT, TRUE
from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt  # crea un token
from core.models import Asistencia, Alumno
from .serializers import AsistenciaSerializer, AlumnoSerializer, UpdateAlumnosSerializer, UpdateAsistenciaSerializer, ChangePasswordSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated   
from random import randrange

# Create your views here.


def get_object(self, pk):
    return response(self.model, pk=pk)

# def put(self, request, id):
#         jd = json.loads(request.body)
#         asistencia = list(Asistencia.objects.filter(id=id).values())
#         asisteciaput = asistencia[0]
#         if len(asistencia) > 0:
#            asistenciaput = Asistencia.objects.get(id=id)   
#            asistenciaput.id_asistencia = jd['id_asistencia']
#            asistenciaput.rut_alumno = jd['rut_alumno']            
#            asistenciaput.codigo_asignatura = jd['codigo_asignatura']            
#            asistenciaput.nombre_asignatura = jd['nombre_asisgnatura']
#            asistenciaput.fecha = jd['fecha']
#            asistenciaput.seccion = jd ['seccion']
#            asistenciaput.sede = jd['sede']
#            asistenciaput.escuela = jd['escuela']
#            asistenciaput.docente = jd['docente']
#            asistenciaput.save()
#            return Response({'message': 'Asistencia actualizada correctamente'}, status=status.HTTP_200_OK)



@csrf_exempt
@api_view(['GET', 'POST', 'PUT'])
def lista_asistencia(request):
    if request.method == 'GET':
        asistencia = Asistencia.objects.all()
        serializer = AsistenciaSerializer(asistencia, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        asistencia_Serializer = AsistenciaSerializer(data=request.data)
        # validación
        if asistencia_Serializer.is_valid():
            asistencia_Serializer.save()
        # Asistencia_data=JSONParser().parse(request)
        # Asistencia_Serializer=AsistenciaSerializer(data=Asistencia_data)
        return Response({'message': 'Asistencia registrada correctamente'}, status=status.HTTP_201_CREATED)
        # actualizar datos
    elif request.method == 'PUT':
          #asistencia = Asistencia.objects.all()
         asistencia_Serializer = UpdateAsistenciaSerializer(data=request.data)
          #validación
         if asistencia_Serializer.is_valid():
             asistencia_Serializer.save()
          #Asistencia_data=JSONParser().parse(request)
          #Asistencia_Serializer=AsistenciaSerializer(data=Asistencia_data)
         return Response({'message': 'Asistencia actualizada correctamente'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT'])
def lista_alumnos(request):
    if request.method == 'GET':
        alumno = Alumno.objects.all()
        serializer = AlumnoSerializer(alumno, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        alumno_Serializer = AlumnoSerializer(data=request.data)
        # validación
        if alumno_Serializer.is_valid():
            alumno_Serializer.save()
        # Asistencia_data=JSONParser().parse(request)
        # Asistencia_Serializer=AsistenciaSerializer(data=Asistencia_data)
        return Response({'message': 'Ingreso exitoso, ya puedes registrar tu asistencia'}, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
          #asistencia = Asistencia.objects.all()
         alumno_Serializer = UpdateAlumnosSerializer(data=request.data)
          #validación
         if alumno_Serializer.is_valid():
             alumno_Serializer.save()
          #Asistencia_data=JSONParser().parse(request)
          #Asistencia_Serializer=AsistenciaSerializer(data=Asistencia_data)
         return Response({'message': 'Alumno actualizado correctamente'}, status=status.HTTP_200_OK)
         

@api_view(['POST', 'GET'])
def usuario_login(request):
    if request.method == 'GET':
        print(request)
        try:
            if is_empty(request.query_params.get("usuario")) or is_empty(request.query_params.get('password')):
                return Response({'message': 'Faltan datos.', 'success': ''}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Faltan datos.', 'success': ''}, status=status.HTTP_200_OK)

        alumnoUsuario = request.query_params.get("usuario")
        alumnoPassword = request.query_params.get("password")


        try:
            alumno = Alumno.objects.get(usuario=alumnoUsuario, contrasena=alumnoPassword)
            alumnoSerializer = AlumnoSerializer(alumno)
            return Response({'message': 'Alumno', 'data': alumnoSerializer.data, 'success': 'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Usuario o Contraseña no valido.', 'success': ''}, status=status.HTTP_200_OK)
        
    # if request.method == 'POST':
    #     Asistencia_data=JSONParser().parse(request)
    #     Asistencia_serializer=AsistenciaSerializer(data=Asistencia_data)
    #     asistencia_data=JSONParser().parse(request)n
    #     return Response("Registrado Correctamente", safe=False)


@api_view(['GET'])
def cambiar_contrasena(request):
    if request.method == 'GET':
        try:
            if is_empty(request.query_params.get("usuario")) or is_empty(request.query_params.get('password')):
                return Response({'message': 'Faltan datos.', 'success': ''}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Faltan datos.', 'success': ''}, status=status.HTTP_200_OK)

        alumnoUsuario = request.query_params.get("usuario")
        alumnoPassword = request.query_params.get("password")

        existeUsuario = False
        try:
            Alumno.objects.get(usuario=alumnoUsuario)
            existeUsuario = True
        except:
            existeUsuario = False
            return Response({'message': 'Usuario no existe', 'success': ''}, status=status.HTTP_200_OK)
            
        if existeUsuario == True:
            alumno = Alumno.objects.get(usuario=alumnoUsuario)
            alumno.contrasena = alumnoPassword
            alumno.save()
            return Response({'message': 'Contraseña Actualizada', 'success': 'OK'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Usuario no existe', 'success': ''}, status=status.HTTP_200_OK)

@api_view(['GET'])
def crear_usuario(request):
    if request.method == 'GET':
        try:
            if  is_empty(request.query_params.get("rut")) or is_empty(request.query_params.get("usuario")) or is_empty(request.query_params.get('password')):
                return Response({'message': 'Faltan datos.', 'success': ''}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Faltan datos.', 'success': ''}, status=status.HTTP_200_OK)

        alumnoRut = request.query_params.get("rut")
        alumnoUsuario = request.query_params.get("usuario")
        alumnoPassword = request.query_params.get("password")

        _alumno = {}
        _alumno['id_alumno'] = randrange(9999)
        _alumno['rut'] = alumnoRut
        _alumno['usuario'] = alumnoUsuario
        _alumno['contrasena'] = alumnoPassword

        alumnoSerializado = AlumnoSerializer(data=_alumno)
        if alumnoSerializado.is_valid():
            alumnoSerializado.save()
            return Response({'message': 'Usuario Creado', 'success': 'OK'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No se logro crear el usuario', 'success': ''}, status=status.HTTP_200_OK)


def is_empty(a):
    return len(a) == 0