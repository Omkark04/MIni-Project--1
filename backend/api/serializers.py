from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserRegisterData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegisterData
        fields = ['user', 'full_name', 'email', 'mobile', 'dob', 'user_type']
        extra_kwargs = {'user': {'write_only': True}}
