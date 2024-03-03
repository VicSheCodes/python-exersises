from celery import Celery

app_with_backend = Celery(
    "tasks",
    broker="redis://localhost:6380/0",
    backend="db+sqlite:///celery_backend.sqlite",
    task_track_started=True,
)

app = app_with_backend
