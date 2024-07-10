from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    address = models.TextField(max_length=200)

class Doctor(models.Model):
    user = models.OneToOneField(BaseUser, on_delete = models.CASCADE, primary_key = True)
    doctor_profile = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(BaseUser, on_delete = models.CASCADE, primary_key = True)
    patient_profile = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.user.username