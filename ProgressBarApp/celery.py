# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProgressBarApp.settings')

# Create a Celery instance
app = Celery('ProgressBarApp')

# Configure Celery with Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all Django apps
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename=r'D:\M Hamza\System Heuristics SE Job (Full Stack Django)\training-internship\tasks\ProgressBarApp\ProgressBarApp\celery\logs\celery.txt'
)