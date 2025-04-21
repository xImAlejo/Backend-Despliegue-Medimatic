from rest_framework import serializers
from apps.user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime, timedelta

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions']
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    def validate_rol(self, value):
        if value not in [1, 2, 3]:
            raise serializers.ValidationError("Rol inválido")
        return value
    
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('username', 'name', 'lastname')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','name','lastname')

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    def to_representation(self, instance):
            return {
            'id': instance['id'],
            'name': instance['name'],
            'username': instance['username'],
        }

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)
    token = serializers.CharField(min_length=6, write_only=True)
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['iat'] = datetime.now()
        token['user'] = user.username
        token['rol'] = user.rol

        return token