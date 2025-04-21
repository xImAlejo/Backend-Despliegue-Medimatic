from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializer import ActivitySerializer
from apps.activity.models import Activity
from rest_framework.decorators import action

class ActivityViewSets(viewsets.ModelViewSet):
    model = Activity
    serializer_class = ActivitySerializer
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
        
        except self.model.DoesNotExist:
            return Response({'message': 'La activity que intenta actualizar no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        try:
            user = self.model.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'Activity eliminado correctamente'}, status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            return Response({'message': 'Activity no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def getActivitiesbyUserId(self,request,pk=None):
       
        self.queryset = self.serializer_class().Meta.model.objects.filter(user_id=pk)
        Activity = self.get_queryset()
        Activity_serializer = self.serializer_class(Activity, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": Activity_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
