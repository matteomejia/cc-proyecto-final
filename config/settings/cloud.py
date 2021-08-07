from .base import *
from .base import env

SECRET_KEY = 'pf-@jxtojga)z+4s*uwbgjrq$aep62-thd0q7f&o77xtpka!_m'

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': env.db('DATABASE_URL')
}

EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
ANYMAIL = {
    "SENDGRID_API_KEY": env.str('SENDGRID_API_KEY')
}


# AWS S3
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")

AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_IS_GZIPPED = True

AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'us-west-2'
AWS_S3_FILE_OVERWRITE = False
AWS_S3_VERIFY = True

STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'config.storages.PublicMediaStorage'

# CELERY
CELERY_BROKER_URL = env.str('REDIS_URL')
CELERY_RESULT_BACKEND = env.str('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Lima'