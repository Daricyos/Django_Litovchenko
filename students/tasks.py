from datetime import datetime, timedelta

from celery import shared_task

from .models import Logger


@shared_task
def delete_logs():
    logs = Logger.objects.filter(created__lte=datetime.now() - timedelta(days=7)).all()
    if not logs:
        return 'Logs older than 7 days not found'
    else:
        logs.delete()
        return 'Logs deleted!'
