from django.contrib import admin
from usr_role.models import BaseUser, Doctor, Patient

# Register your models here.
admin.site.register(BaseUser)
admin.site.register(Doctor)
admin.site.register(Patient)