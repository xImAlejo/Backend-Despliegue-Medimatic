from rest_framework import serializers
from apps.coordination.models import Coordination

class CoordinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordination
        fields = '__all__'