from rest_framework import generics
from .models import persondetails, marks
from .serializers import persondetailsserializer, marksserializer, Userserializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class persondetailslist(generics.ListCreateAPIView):
    queryset = persondetails.objects.all()
    serializer_class = persondetailsserializer
    permission_classes = [IsAuthenticated]


class marksdetailslist(generics.ListCreateAPIView):
    queryset = marks.objects.all()
    serializer_class = marksserializer


class persondetailsview(generics.RetrieveUpdateDestroyAPIView):
    queryset = persondetails.objects.all()
    serializer_class = persondetailsserializer


class marksdetailsview(generics.RetrieveUpdateDestroyAPIView):
    queryset = marks.objects.all()
    serializer_class = marksserializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
