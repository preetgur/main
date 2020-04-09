from django.db import models
from django.contrib.auth.models import User  # Exteding User built in models 
# In settings.py  configure "AUTH_USER_MODEL = 'student.User'"


class User(models.Model):

    is_student = models.BooleanField()
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.user.username