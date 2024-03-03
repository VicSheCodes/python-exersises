from celery import Celery


app = Celery("tasks", broker="redis://localhost:6380/0", task_track_started=True)
