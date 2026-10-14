from app.tasks.celery_app import celery


@celery.task(name="tasks.generate_meeting_summary")
def generate_meeting_summary(meeting_id: str, transcript: str):
    """Async task to generate meeting summary and action items."""
    pass


@celery.task(name="tasks.redact_meeting_transcript")
def redact_meeting_transcript(meeting_id: str):
    """Async task to redact sensitive data from transcripts."""
    pass
