from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.db import DatabaseError

from .models import Libro
from .serializers import LibroSerializer

class Login(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
        

class Logout(APIView):

    def post(self, request):
        try:
            token = request.data["token"]
            Token.objects.get(key=token).delete()

            return Response({'message': 'token eliminado'},status=status.HTTP_200_OK)
        except DatabaseError as e:
            return Response({'message: ': e.__str__}, status=status.HTTP_400_BAD_REQUEST)

class LibroList(APIView):
    def get(self, request):
        libros = Libro.objects.all()

        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)

class LibroSelect(APIView):

    serializer_class = LibroSerializer

    def get(self, request, id):        
        try:
            libro = Libro.objects.get(pk = id)
        
            serializer = LibroSerializer(libro, many=False)
            return Response(serializer.data)
        except DatabaseError as e:
            return Response({'message': e.__str__}, status=status.HTTP_400_BAD_REQUEST)

class LibroCreate(APIView):

    def post(self, request):

        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Libro creado'}, status=status.HTTP_201_CREATED)

class LibroUpdate(APIView):
    def put(self, request, id, pk=None):
        try:
            libro = Libro.objects.get(pk=id)
            serializer = LibroSerializer(instance=libro, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Libro Actualizado'}, status=status.HTTP_200_OK)
        except DatabaseError as e:
            return Response({'message': e.__str__}, status=status.HTTP_400_BAD_REQUEST)

class LibroDelete(APIView):

    def delete(self, request, id, pk=None):
        try:
            libro = Libro.objects.get(pk=id).delete()
            return Response({"message": "Libro Eliminado"}, status=status.HTTP_200_OK)
        except DatabaseError as e:
            return Response({'message': e.__str__}, status=status.HTTP_400_BAD_REQUEST)

        