from rest_framework import serializers
from .models import Company, Internship, StudentProfile, Application, SavedInternship
class CompanySerializer(serializers.ModelSerializer):
    class Meta: model=Company; fields='__all__'
class InternshipSerializer(serializers.ModelSerializer):
    company_name=serializers.CharField(source='company.name',read_only=True)
    company_logo=serializers.CharField(source='company.logo',read_only=True)
    class Meta: model=Internship; fields='__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta: model=StudentProfile; fields='__all__'
class ApplicationSerializer(serializers.ModelSerializer):
    internship_title=serializers.CharField(source='internship.title',read_only=True)
    company_name=serializers.CharField(source='internship.company.name',read_only=True)
    class Meta: model=Application; fields='__all__'
class SavedSerializer(serializers.ModelSerializer):
    class Meta: model=SavedInternship; fields='__all__'
