from app.tasks.celery_app import celery


@celery.task(name="tasks.sync_platform_meetings")
def sync_platform_meetings(org_id: str):
    """Background task to sync upcoming meetings from connected providers."""
    pass


@celery.task(name="tasks.process_meeting_security_scan")
def process_meeting_security_scan(meeting_id: str):
    """Background task to analyze live meeting metadata for security risks."""
    pass
