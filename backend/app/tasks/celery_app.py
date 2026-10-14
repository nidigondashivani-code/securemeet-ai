from celery import Celery
from app.core.config import settings

celery = Celery(
    "securemeet_worker",
    broker=str(settings.CELERY_BROKER_URL or settings.REDIS_URL),
    backend=str(settings.CELERY_RESULT_BACKEND or settings.REDIS_URL),
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=3600,  # 1 hour max for large transcripts
)

celery.autodiscover_tasks(["app.tasks.meeting_tasks", "app.tasks.ai_tasks"])
