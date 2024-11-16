from celery import Celery


app = Celery('project', broker='redis://redis:6379/0')

app.autodiscover_tasks(['project'])