import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot.settings')

app = Celery('robot')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my_schedule': {
        'task': 'user.tasks.print_user_count',
        'schedule': 60,
        'args': (),
        'kwargs': {},
    }
}
