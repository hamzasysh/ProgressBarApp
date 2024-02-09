from celery import shared_task
from celery_progress.backend import ProgressRecorder
import time

@shared_task(bind=True)
def my_task(self):
    progress_recorder = ProgressRecorder(self)
    result = 0
    for i in range(10):
        print('mytask is running')
        time.sleep(1)
        result += i
        progress_recorder.set_progress(i + 1, 10)
    return result