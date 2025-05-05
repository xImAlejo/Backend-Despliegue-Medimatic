from rest_framework import serializers
from apps.product.models import Product
from apps.serie.models import Serie
from apps.entry.models import Entry
from apps.serie.api.serializer import SerieSerializer
import re

class ProductSerializer(serializers.ModelSerializer):
    series_input = serializers.CharField(write_only=True)  # campo para ingresar series como texto

    class Meta:
        model = Product
        fields = [
            'id', 'type', 'imported', 'description', 'brand', 'unit_price', 'type_change', 
            'bill_text', 'date_bill', 'model', 'origin', 'date_manufacture', 'minsa_code', 
            'minsa_description', 'supplier', 'entry_point', 'exit_point', 'date', 'entry_guide', 'exit_guide', 
            'proyect', 'responsible', 'coin_bill', 'series_input'
        ]

    def validate(self, data):
        series_input = data.get('series_input', '')
        series_list = [s.strip() for s in re.split(r'[;,]', series_input) if s.strip()]

        # Guardamos para usar en create()
        data['series_list'] = series_list
        return data

    def create(self, validated_data):
        series_list = validated_data.pop('series_list')
        validated_data.pop('series_input')  # ya no lo necesitamos
        product = Product.objects.create(**validated_data)

        for serie_name in series_list:
            serie = Serie.objects.create(name=serie_name, product=product)
            Entry.objects.create(serie=serie)

        return product