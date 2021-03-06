import os
from celery import Celery
from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restProject.settings')

app = Celery('restProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-every-2-seconds': {
#         'task': 'some_task',
#         'schedule': crontab("2")
#     }
# }


# @app.task(bind=True)
# def debug_task(self):
#     print("hello world")
#     print('Request: {0!r}'.format(self.request))
