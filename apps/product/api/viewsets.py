from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializer import ProductSerializer
from apps.product.models import Product
from rest_framework.decorators import action

class ProductViewSets(viewsets.ModelViewSet):
    model = Product
    serializer_class = ProductSerializer
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
        
        except Product.DoesNotExist:
            return Response({'message': 'El product que intenta actualizar no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        try:
            user = self.model.objects.get(pk=pk)
            user.delete()
            return Response({'message': 'Product eliminado correctamente'}, status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            return Response({'message': 'Product no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['put'])
    def UpdateQuantityEnter(self, request, pk=None):
        try:
            product = self.get_object(pk)
        except Product.DoesNotExist:
            return Response({'message': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        quantity_enter = request.data.get('quantity_enter')

        if quantity_enter is None:
            return Response({'error': 'Se requiere el campo quantity_enter'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product.quantity_enter = int(quantity_enter)
            product.save()
            return Response({'quantity_enter': product.quantity_enter}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'El valor de quantity_enter debe ser un número entero'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['put'])
    def UpdateQuantityExit(self, request, pk=None):
        try:
            product = self.get_object(pk)
        except Product.DoesNotExist:
            return Response({'message': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        quantity_exit = request.data.get('quantity_exit')

        if quantity_exit is None:
            return Response({'error': 'Se requiere el campo quantity_exit'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product.quantity_exit = int(quantity_exit)
            product.save()
            return Response({'quantity_exit': product.quantity_exit}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'El valor de quantity_exit debe ser un número entero'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['put'])
    def UpdateExitandProyectandGuideandExitDate(self, request, pk=None):
        try:
            product = self.get_object(pk)
        except Product.DoesNotExist:
            return Response({'message': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        exit_point = request.data.get('exit_point')
        proyect = request.data.get('proyect')
        exit_guide = request.data.get('exit_guide')
        exit_date = request.data.get('exit_date')
        origin = request.data.get('origin')
        quantity_total_exit = request.data.get('quantity_total_exit')  

        try:
            product.exit_point = exit_point
            product.proyect = proyect
            product.exit_guide = exit_guide
            product.exit_date = exit_date
            product.origin = origin
            product.quantity_total_exit = quantity_total_exit
            product.save()
            return Response({'exit_point': product.exit_point,'proyect': product.proyect, 'exit_guide':product.exit_guide, 'exit_date':product.exit_date, 'origin': product.origin}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'El valor de exit_point, proyect, exit_guide, exit_date o origin no esta bien colocado'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['put'])
    def UpdateDatesandSupplierandEnterPointandEnterGuide(self, request, pk=None):
        try:
            product = self.get_object(pk)
        except Product.DoesNotExist:
            return Response({'message': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        date_manufacture = request.data.get('date_manufacture')
        date = request.data.get('date')
        date_bill =  request.data.get('date_bill')
        bill_text = request.data.get('bill_text')
        supplier = request.data.get('supplier')
        entry_point = request.data.get('entry_point')
        entry_guide = request.data.get('entry_guide')
        proyect = request.data.get('proyect')
        origin = request.data.get('origin')
        quantity_total = request.data.get('quantity_total')
        
        try:
            product.date_manufacture = date_manufacture
            product.date = date
            product.proyect = proyect
            product.date_bill = date_bill
            product.bill_text = bill_text
            product.supplier = supplier
            product.entry_point = entry_point
            product.entry_guide = entry_guide
            product.origin = origin
            product.quantity_total = quantity_total
            product.save()
            return Response({'date_manufacture': product.date_manufacture,'date': product.date, 'proyect':product.proyect, 'date_bill':product.date_bill, 'supplier':product.supplier, 'entry_point':product.entry_point, 'entry_guide':product.entry_guide, 'origin':product.origin, 'bill_text':product.bill_text}, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'El valor de date_manufacture, date, proyect, date_bill, supplier, entry_point, entry_guide, origin o bill_text no esta bien colocado'}, status=status.HTTP_400_BAD_REQUEST)