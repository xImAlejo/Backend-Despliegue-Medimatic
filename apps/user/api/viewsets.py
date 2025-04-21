from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializer import UserSerializer
from apps.user.models import User
from rest_framework.decorators import action
from .serializer import PasswordSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated
from apps.user.api.serializer import (
    CustomTokenObtainPairSerializer, CustomUserSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 2
    
class UserViewSets(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = None
    #permission_classes = [IsAuthenticated]
    permission_clases = [AllowAny]

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.get_serializer().Meta.model.objects
        return self.queryset
    
    def list(self,request):
        user_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "rows": user_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        section = self.get_object(pk)
        user_serializer = self.serializer_class(section)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        try:
            user = self.get_object(pk)
            serializer = self.serializer_class(user, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response({'message': 'Datos inválidos', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            return Response({'message': 'El user que intenta actualizar no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        try:
            user = self.model.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'])
    def set_password(self, request,pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': 'Contraseña actualizada correctamente'
            })
        return Response({
            'message': 'Hay errores en la información enviada',
            'errors': password_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class SetPassword(viewsets.GenericViewSet):
    serializer_class = PasswordSerializer
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user =  User.objects.filter(is_active=True).get(token_password=serializer.validated_data['token'])
            user.set_password(serializer.validated_data['password'])
            user.token_password = None 
            user.save()
            return Response({
                'message': 'contraseña cambiada'
            })
        else:
                
            return Response({'message':'errror'},status= status.HTTP_400_BAD_REQUEST)

# Login view for users.
class Login(TokenObtainPairView):
      serializer_class = CustomTokenObtainPairSerializer
      def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Login Succesful'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)