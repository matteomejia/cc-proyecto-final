from celery import Celery
from celery.schedules import crontab

from core.models import CeleryResult
from workshops.models import Workshop
from store.models import Inscription, Order
from users.models import User, Student

import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.cloud')

app = Celery('cloud')
app.config_from_object(
    'django.conf:settings',
    namespace='CELERY'
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=12, day_of_week=1), get_metrics(), name='send feedback mail')


@app.task()
def get_metrics(self):
    earnings = 0
    for elem in Order.objects.filter(paid=True):
        earnings += elem.get_total()
    results = {
        'total_inscriptions': Inscription.objects.filter(paid=True).count(),
        'total_students': Student.objects.all().count(),
        'earnings': earnings
    }

    metrics = CeleryResult.objects.create(results=results)
    metrics.save()