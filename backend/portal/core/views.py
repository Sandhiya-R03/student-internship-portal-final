from django.http import JsonResponse


INTERNSHIPS = [
    {
        "id": 1,
        "title": "Frontend Developer Intern",
        "company": "TechNova Solutions",
        "location": "Chennai",
        "mode": "Hybrid",
        "stipend": "₹15,000/month",
        "duration": "3 Months",
        "skills": ["React", "JavaScript", "HTML", "CSS"],
        "category": "Web Development",
    },
    {
        "id": 2,
        "title": "Python Django Intern",
        "company": "CodeCraft Technologies",
        "location": "Bangalore",
        "mode": "Remote",
        "stipend": "₹18,000/month",
        "duration": "6 Months",
        "skills": ["Python", "Django", "REST API"],
        "category": "Backend Development",
    },
    {
        "id": 3,
        "title": "Data Science Intern",
        "company": "DataSphere",
        "location": "Coimbatore",
        "mode": "On-site",
        "stipend": "₹12,000/month",
        "duration": "4 Months",
        "skills": ["Python", "Pandas", "Machine Learning"],
        "category": "Data Science",
    },
    {
        "id": 4,
        "title": "Java Developer Intern",
        "company": "InnovateTech",
        "location": "Chennai",
        "mode": "Hybrid",
        "stipend": "₹16,000/month",
        "duration": "3 Months",
        "skills": ["Java", "Spring Boot", "MySQL"],
        "category": "Software Development",
    },
]


COMPANIES = [
    {
        "id": 1,
        "name": "TechNova Solutions",
        "location": "Chennai",
        "industry": "Technology",
    },
    {
        "id": 2,
        "name": "CodeCraft Technologies",
        "location": "Bangalore",
        "industry": "Software",
    },
    {
        "id": 3,
        "name": "DataSphere",
        "location": "Coimbatore",
        "industry": "Data & AI",
    },
    {
        "id": 4,
        "name": "InnovateTech",
        "location": "Chennai",
        "industry": "Technology",
    },
]


def internships(request):
    return JsonResponse(INTERNSHIPS, safe=False)


def companies(request):
    return JsonResponse(COMPANIES, safe=False)