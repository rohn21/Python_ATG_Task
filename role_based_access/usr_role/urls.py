from django.urls import path
from .import  views
from django.views.generic import TemplateView

app_name = 'usr_role'

urlpatterns=[
    path('success/', TemplateView.as_view(template_name='user_role/success.html'), name='success'),
    path('register/', views.DoctorRegisteration.as_view(), name='register'),
]