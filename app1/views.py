from rest_framework import generics
from .models import student, course
from .serializers import studentserializer, courseserializer, Userserializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class studentlist(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer
    permission_classes = [IsAuthenticated]


class courselist(generics.ListCreateAPIView):
    queryset = course.objects.all()
    serializer_class = courseserializer


class studentview(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer


class courseview(generics.RetrieveUpdateDestroyAPIView):
    queryset = course.objects.all()
    serializer_class = courseserializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer