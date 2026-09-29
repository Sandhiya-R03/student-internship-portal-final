SECRET_KEY = "student-internship-portal-secret-key"

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

ROOT_URLCONF = "portal.urls"

INSTALLED_APPS = [
    "django.contrib.staticfiles",
]

MIDDLEWARE = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy",
    }
}

STATIC_URL = "static/"