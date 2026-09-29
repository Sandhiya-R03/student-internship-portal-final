from django.contrib import admin
from .models import Company, Internship, StudentProfile, Application, SavedInternship
admin.site.register([Company,Internship,StudentProfile,Application,SavedInternship])
