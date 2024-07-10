from django.urls import path
from .import  views
from django.views.generic import TemplateView

app_name = 'usr_role'

urlpatterns=[
    path('success/', TemplateView.as_view(template_name='user_role/success.html'), name='success'),
    path('doctor/', views.DoctorRegisteration.as_view(), name='doctor_register'),
    path('patient/', views.PatientRegisteration.as_view(), name='patient_register'),
    path('register/', TemplateView.as_view(template_name='user_role/register.html'), name='register'),
]