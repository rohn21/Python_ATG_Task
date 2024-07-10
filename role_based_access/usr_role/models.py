from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group
from django.contrib.auth.base_user import BaseUserManager

# class CustomUserManager(BaseUserManager):

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not email:
#             raise ValueError("The given email must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError(
#                 "Superuser must have is_staff=True."
#             )
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError(
#                 "Superuser must have is_superuser=True."
#             )

#         return self._create_user(email, password, **extra_fields)
    

# Create your models here.
# GENDER_CHOICES = {
#     'M': 'Male',
#     'F': 'Female',
#     'NA': 'Not Specified',
# }

class BaseUser(User):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    address = models.TextField(max_length=200)

class Doctor(models.Model):
    user = models.OneToOneField(BaseUser, on_delete = models.CASCADE, primary_key = True)
    doctor_profile = models.ImageField(upload_to='profiles/', blank=True)

class Patient(models.Model):
    user = models.OneToOneField(BaseUser, on_delete = models.CASCADE, primary_key = True)
    patient_profile = models.ImageField(upload_to='profiles/', blank=True)