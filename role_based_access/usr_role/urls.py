from django.urls import path
from .import  views
from django.views.generic import TemplateView

app_name = 'usr_role'

urlpatterns=[
    path('success/', TemplateView.as_view(template_name='user_role/success.html'), name='success'),
    path('doctor/', views.DoctorRegisteration.as_view(), name='doctor_register'),
    path('patient/', views.PatientRegisteration.as_view(), name='patient_register'),
    path('login/',views.LoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('register/', TemplateView.as_view(template_name='user_role/register.html'), name='register'),
    path('patient-home/', views.PatientDashboardView.as_view(), name='patient'),
    path('doctor-home/', views.DoctorDashboardView.as_view(), name='doctor'),
    # path('patient-home/', TemplateView.as_view(template_name='user_role/patient_dashboard.html'), name='patient'),
    # path('doctor-home/', TemplateView.as_view(template_name='user_role/doctor_dashboard.html'), name='doctor'),
]