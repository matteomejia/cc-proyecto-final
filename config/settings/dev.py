from .base import *
import environ

env = environ.Env()
env.read_env(str(BASE_DIR / '.env'))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Database
DATABASES = {
    'default': env.db("DATABASE_URL")
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'mailhog'
EMAIL_PORT = 1025