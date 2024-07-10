from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    school_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username