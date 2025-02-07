from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'examen', 'level']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Encripta la contraseña
        return User.objects.create(**validated_data)
