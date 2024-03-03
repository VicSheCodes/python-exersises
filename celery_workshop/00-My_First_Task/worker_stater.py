from our_celery_app import app
import tasks

argv = ["worker", "--loglevel", "info", "--concurrency", "1"]
app.worker_main(argv)
