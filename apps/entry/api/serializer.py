from rest_framework import serializers
from apps.entry.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

    def validate_quantity(self, value):
        # Permitir null como un valor válido
        if value == '':
            return None
        return value