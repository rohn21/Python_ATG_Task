from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, RedirectView, TemplateView
from usr_role.models import BaseUser, Doctor, Patient
from usr_role.forms import UserCreationForm, DoctorSignUpForm, PatientSignUpForm

# Create your views here.


class DoctorRegisteration(CreateView):
    model = Doctor
    form_class = DoctorSignUpForm()
    template_name = 'user_role/doctor_register.html'
    success_url = reverse_lazy('usr_role:success')
    success_message = 'Congratulation, Registration successful | Please login to continue !!!!'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)