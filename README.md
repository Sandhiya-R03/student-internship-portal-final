# InternSphere — Student Internship Portal

A final-year-style full-stack student internship portal built with **React JS + Python Django REST Framework + MySQL**.

## Modules included
- Student landing page with creative responsive UI
- Internship search by role, skill, company or location
- Category and work-mode filters
- Featured internship cards
- Internship details/navigation foundation
- Student profile with skills and profile strength
- Application tracking with status timeline
- Saved internship UI
- Company and internship REST APIs
- Dashboard statistics API
- Django admin panel
- Demo data seeding command
- Responsive design for desktop, tablet and mobile

## Folder structure
```
student-internship-portal/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env.example
│   └── portal/
└── frontend/
    ├── package.json
    ├── index.html
    └── src/
```

## 1. MySQL setup
Create a database in MySQL:
```sql
CREATE DATABASE student_internship_portal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 2. Backend setup (VS Code terminal)
Open the `backend` folder in a terminal.

Windows:
```powershell
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and enter your MySQL password.

Then:
```powershell
python manage.py makemigrations core
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```
Backend: http://127.0.0.1:8000
API: http://127.0.0.1:8000/api/internships/
Admin: http://127.0.0.1:8000/admin/

## 3. Frontend setup
Open a second VS Code terminal and open the `frontend` folder:
```powershell
npm install
npm run dev
```
Open the Vite URL shown in the terminal, normally:
http://localhost:5173

## Demo login
The current student UI uses a demo profile (Arun Kumar) to keep the academic project easy to run. Authentication can be added as a next module using Django JWT/session authentication.

## Suggested viva/project extension modules
1. JWT login/register
2. Company login and company dashboard
3. Resume upload and parsing
4. Aptitude/skill assessment
5. Interview scheduling
6. Email notifications
7. Internship recommendation engine
8. Application analytics
9. Certificate generation after internship completion
10. College placement officer dashboard
