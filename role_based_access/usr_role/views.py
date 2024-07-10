from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout,authenticate
from django.views.generic import CreateView, RedirectView, TemplateView, FormView
from usr_role.models import BaseUser, Doctor, Patient
from usr_role.forms import UserCreationForm, DoctorSignUpForm, PatientSignUpForm, LoginForm

# Create your views here.
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user_role/login.html'

    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

         # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)
        
    def get_success_url(self):
        if self.request.user.is_patient:
            return reverse_lazy('usr_role:patient')
        elif self.request.user.is_doctor:
            return reverse_lazy('usr_role:doctor')
        else:
            return reverse_lazy('usr_role:login')

class DoctorRegisteration(CreateView):
    model = Doctor
    form_class = DoctorSignUpForm
    template_name = 'user_role/doctor_register.html'
    success_url = reverse_lazy('usr_role:login')
    success_message = 'Congratulation, Registration successful | Please login to continue !!!!'

    # for directly redirect to userpage after user_registration
    def form_valid(self, form):
        form.save()
        user = form.save()
        login(self.request, user)
        return redirect('usrs:teacher')

class PatientRegisteration(CreateView):
    model = Patient
    form_class = PatientSignUpForm
    template_name = 'user_role/patient_register.html'
    success_url = reverse_lazy('usr_role:login')
    success_message = 'Congratulation, Registration successful | Please login to continue !!!!'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class PatientDashboardView(TemplateView):
    template_name = 'user_role/patient_dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if not authenticated
        if not request.user.is_patient:
            return redirect('home')  # Redirect to home if not a patient
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_image'] = self.request.user.patient.patient_profile.url  # Assuming 'profile_image' in custom user model
        # Add other relevant data for the patient dashboard here
        return context

class DoctorDashboardView(TemplateView):
    template_name = 'user_role/doctor_dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('usr_role:login')  # Redirect to login if not authenticated
        if not request.user.is_doctor:
            return redirect('usr_role:login')  # Redirect to home if not a patient
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_image'] = self.request.user.doctor.doctor_profile.url  # Assuming 'profile_image' in custom user model
        # Add other relevant data for the patient dashboard here
        return context

class LogoutView(RedirectView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('usr_role:login'))