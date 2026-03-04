from django.db import models
from django.contrib.auth.models import User


class student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class course(models.Model):
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    student = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name