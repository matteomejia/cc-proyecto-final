from .base import *
from .base import env

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Database
DATABASES = {
    'default': env.db("DATABASE_URL")
}