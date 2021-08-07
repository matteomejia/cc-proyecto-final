from celery import Celery

import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.cloud')

app = Celery('cloud')
app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)