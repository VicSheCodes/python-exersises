from our_celery_app import app
import tasks

argv = ["worker", "--loglevel", "info", "--concurrency", "5"]
app.worker_main(argv)
