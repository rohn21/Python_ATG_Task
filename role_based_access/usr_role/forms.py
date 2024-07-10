from django import forms
from usr_role.models import BaseUser, Doctor, Patient
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class UserCreationForm(forms.Modelform):
#     class Meta:
#         model = BaseUser
#         fields = "__all__"

# class DoctorRegistrationForm(UserCreationForm):
#     user_profile = UserCreationForm()

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user_profile = self.cleaned_data['user_profile']
#         if commit:
#             user.save()
#             user_profile.save(commit=False)
#             user_profile.instance.user = user
#             user_profile.save()
#         return user

# class PatientRegistrationForm(UserCreationForm):
#     user_profile = UserCreationForm()

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user_profile = self.cleaned_data['user_profile']
#         if commit:
#             user.save()
#             user_profile.save(commit=False)
#             user_profile.instance.user = user
#             user_profile.save()
#         return user  
        


class PatientSignUpForm(UserCreationForm):
    patient_profile = forms.ImageField()

    class Meta(UserCreationForm.Meta):
        model = BaseUser
        fields = ("patient_profile", "first_name", "last_name", "email", "username", "password1", "password2", "address")
    
    # @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.username = self.cleaned_data.get('username')
        user.save()

        patient_profile = self.cleaned_data['patient_profile']
        if patient_profile:
            patient = Patient.objects.create(user=user, patient_profile=patient_profile)
            patient.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    doctor_profile = forms.ImageField()

    class Meta(UserCreationForm.Meta):
        model = BaseUser
        fields = ("doctor_profile", "first_name", "last_name", "email", "username", "password1", "password2", "address")

    # @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_staff = True
        user.username = self.cleaned_data.get('username')
        user.save()

        doctor_profile = self.cleaned_data['doctor_profile']
        if doctor_profile:
            doctor = Doctor.objects.create(user=user, doctor_profile=doctor_profile)
            doctor.save()
        return user