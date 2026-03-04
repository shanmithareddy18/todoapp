from rest_framework import serializers
from .models import student, course
from django.contrib.auth.models import User


class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class courseserializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user