from django.urls import path
from portal.core import views

urlpatterns = [
    path("api/internships/", views.internships, name="internships"),
    path("api/companies/", views.companies, name="companies"),
]