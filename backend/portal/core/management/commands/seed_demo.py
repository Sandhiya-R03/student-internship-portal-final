from datetime import date,timedelta
from django.core.management.base import BaseCommand
from portal.core.models import Company, Internship, StudentProfile, Application
class Command(BaseCommand):
    help='Seed demo internship portal data'
    def handle(self,*args,**kwargs):
        Company.objects.all().delete(); Internship.objects.all().delete(); StudentProfile.objects.all().delete(); Application.objects.all().delete()
        companies=[
            ('NovaTech','NT','Bengaluru','Building intelligent products for modern teams.'),('PixelForge','PF','Chennai','Design and engineering studio focused on delightful digital experiences.'),('CloudNest','CN','Hyderabad','Cloud-native solutions for growing businesses.'),('DataOrbit','DO','Pune','Data and analytics products for enterprise teams.'),('FinEdge','FE','Mumbai','Technology-led financial services and platforms.')]
        cs=[]
        for n,l,loc,a in companies: cs.append(Company.objects.create(name=n,logo=l,location=loc,about=a))
        data=[
        ('Frontend Developer Intern',cs[0],'Web Development','Bengaluru','Hybrid','₹15,000 / month',['React','JavaScript','CSS','Git'],True),
        ('Python Django Intern',cs[2],'Backend Development','Hyderabad','Remote','₹12,000 / month',['Python','Django','REST API','MySQL'],True),
        ('UI/UX Design Intern',cs[1],'UI/UX','Chennai','On-site','₹10,000 / month',['Figma','Wireframing','Prototyping'],False),
        ('Data Analyst Intern',cs[3],'Data Science','Pune','Hybrid','₹14,000 / month',['Python','Pandas','SQL','Power BI'],True),
        ('Full Stack Developer Intern',cs[4],'Full Stack','Mumbai','Remote','₹18,000 / month',['React','Django','MySQL','REST API'],True),
        ('Cloud Engineering Intern',cs[2],'Cloud','Hyderabad','Hybrid','₹16,000 / month',['AWS','Linux','Docker','Git'],False),
        ('Java Developer Intern',cs[0],'Software Development','Bengaluru','On-site','₹13,000 / month',['Java','Spring Boot','SQL'],False),
        ('AI/ML Research Intern',cs[3],'AI / ML','Pune','Remote','₹20,000 / month',['Python','Machine Learning','Pandas'],True)]
        for title,c,cat,loc,mode,stip,skills,feat in data:
            Internship.objects.create(title=title,company=c,category=cat,location=loc,work_mode=mode,stipend=stip,skills=skills,description=f'Work with the {c.name} team on production-oriented projects, learn industry workflows and build a portfolio-ready internship experience.',responsibilities=['Build and improve assigned features','Collaborate with mentors and developers','Write clean, maintainable code','Participate in reviews and demos'],deadline=date.today()+timedelta(days=20),featured=feat,applicants=12)
        student=StudentProfile.objects.create(name='Arun Kumar',email='arun@example.com',college='ABC Institute of Technology',course='B.Tech Artificial Intelligence & Machine Learning',year='3rd Year',skills=['React','Python','Django','MySQL','Git'],bio='Passionate student developer looking for a hands-on internship opportunity.')
        Internship.objects.all().first().applications.create(student=student,cover_note='Excited to learn and contribute.')
        self.stdout.write(self.style.SUCCESS('Demo data created successfully.'))
