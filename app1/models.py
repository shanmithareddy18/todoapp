from django.db import models
from django.contrib.auth.models import User


class persondetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class marks(models.Model):
    person = models.ForeignKey(persondetails, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return self.subject