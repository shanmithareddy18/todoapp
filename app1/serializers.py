from rest_framework import serializers
from .models import persondetails, marks
from django.contrib.auth.models import User


class persondetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = persondetails
        fields = '__all__'


class marksserializer(serializers.ModelSerializer):
    class Meta:
        model = marks
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