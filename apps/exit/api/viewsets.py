from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializer import ExitSerializer
from apps.exit.models import Exit
from rest_framework.decorators import action

class ExitViewSets(viewsets.ModelViewSet):
    model = Exit
    serializer_class = ExitSerializer
    queryset = None

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
        
        except Exit.DoesNotExist:
            return Response({'message': 'Los Exits que intenta actualizar no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        try:
            user = self.model.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'Exit eliminado correctamente'}, status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            return Response({'message': 'Exit no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def getExitsbySerieId(self,request,pk=None):
       
        self.queryset = self.serializer_class().Meta.model.objects.filter(serie_id=pk)
        exits = self.get_queryset()
        exits_serializer = self.serializer_class(exits, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": exits_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['put'])
    def UpdateQuantityBySerieId(self, request, pk=None):
        try:
            exit = self.serializer_class().Meta.model.objects.get(serie_id=pk)
        except Exit.DoesNotExist:
            return Response({'message': 'Exit no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        quantity = request.data.get('quantity')

        if quantity is None:
            return Response({'error': 'Se requiere el campo quantity'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            exit.quantity = int(quantity)
            exit.save()
            return Response({'quantity': exit.quantity}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'El valor de quantity debe ser un número entero'}, status=status.HTTP_400_BAD_REQUEST)