import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINS_MODULE', 'Board_pst.settings')

app = Celery('Board_pst')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'posts.tasks.send_email_subscribers',
        'schedule': 10,
        'args': (),
    },
}



















