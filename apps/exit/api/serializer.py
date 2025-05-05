from rest_framework import serializers
from apps.exit.models import Exit

class ExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exit
        fields = '__all__'
    
    def validate_quantity(self, value):
        # Permitir null como un valor válido
        if value == '':
            return None
        return value