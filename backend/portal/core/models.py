from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=120)
    logo=models.CharField(max_length=10, default='CO')
    location=models.CharField(max_length=120)
    website=models.URLField(blank=True)
    about=models.TextField(blank=True)
    def __str__(self): return self.name

class Internship(models.Model):
    WORK_MODES=[('Remote','Remote'),('Hybrid','Hybrid'),('On-site','On-site')]
    TYPES=[('Paid','Paid'),('Unpaid','Unpaid')]
    title=models.CharField(max_length=160)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='internships')
    category=models.CharField(max_length=80)
    location=models.CharField(max_length=120)
    work_mode=models.CharField(max_length=20,choices=WORK_MODES,default='Remote')
    stipend=models.CharField(max_length=80,default='₹10,000 / month')
    internship_type=models.CharField(max_length=20,choices=TYPES,default='Paid')
    duration=models.CharField(max_length=60,default='3 Months')
    skills=models.JSONField(default=list)
    description=models.TextField()
    responsibilities=models.JSONField(default=list)
    deadline=models.DateField()
    featured=models.BooleanField(default=False)
    applicants=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class StudentProfile(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    college=models.CharField(max_length=180)
    course=models.CharField(max_length=120)
    year=models.CharField(max_length=30,default='3rd Year')
    skills=models.JSONField(default=list)
    bio=models.TextField(blank=True)
    resume_url=models.URLField(blank=True)
    def __str__(self): return self.name

class Application(models.Model):
    STATUS=[('Applied','Applied'),('Under Review','Under Review'),('Shortlisted','Shortlisted'),('Interview','Interview'),('Selected','Selected'),('Rejected','Rejected')]
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='applications')
    internship=models.ForeignKey(Internship,on_delete=models.CASCADE,related_name='applications')
    status=models.CharField(max_length=30,choices=STATUS,default='Applied')
    cover_note=models.TextField(blank=True)
    applied_at=models.DateTimeField(auto_now_add=True)
    class Meta: unique_together=('student','internship')

class SavedInternship(models.Model):
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='saved')
    internship=models.ForeignKey(Internship,on_delete=models.CASCADE,related_name='saved_by')
    saved_at=models.DateTimeField(auto_now_add=True)
    class Meta: unique_together=('student','internship')
